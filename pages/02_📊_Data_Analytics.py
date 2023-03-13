import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from streamlit_extras.app_logo import add_logo



# Imported Budget.csv
Budget = pd.read_csv('Budget.csv')




url1="https://drive.google.com/file/d/12NQM8wBzIl3XwJqAGLZnZ3r3El9A6hyq/view?usp=sharing"
pacclogo='https://drive.google.com/uc?export=download&id='+url1.split('/')[-2]

st.set_page_config(
     page_title="Analytical Tool",
     layout="wide",
     page_icon= pacclogo,
    initial_sidebar_state="expanded")
url1="https://drive.google.com/file/d/12NQM8wBzIl3XwJqAGLZnZ3r3El9A6hyq/view?usp=sharing"
pacclogo='https://drive.google.com/uc?export=download&id='+url1.split('/')[-2]


add_logo(pacclogo,height=200)

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

show_streamlit_style = """
            <style>
            footer:after {
                content:'Developed By Karim Hazime';
                visibility: visible;}
            </style>
            """
st.markdown(show_streamlit_style, unsafe_allow_html=True)

#function to read large data with caching
@st.cache_data()
def load_data(path):
    df=pd.read_csv(path)
    return df

sales_product=load_data('https://www.dropbox.com/s/70qklgbeyurk9hs/Sales.csv?dl=1')


#read the 2nd dataframe
url2 = 'https://drive.google.com/file/d/1KlN6GLxMRJ2cyS057vl3E2l1BfxoaG0R/view?usp=sharing'
path2 = 'https://drive.google.com/uc?export=download&id='+url2.split('/')[-2]
Sales_Daily=load_data(path2)

sales_product = sales_product[sales_product['Product Key'].notnull()]
Sales_Daily['Transaction Date'] = pd.to_datetime(Sales_Daily['Transaction Date'], format='%d/%m/%Y', errors='coerce')
sales_product['Supp_Story'] = sales_product['Supp_Story'].str.capitalize()
tab1, tab2 = st.tabs(["Sales Overview Dashboard", "A Comparative Study of Sales management"])
with tab1:
    expander = st.expander("Insights")
    expander.write("""This dashboard will give a closer look at sales of Coco uae from different perspectives: \n 
* __Graph 1__: By using the slider, you will be able to interact with the trend of time-series sales per day and under each year.
* __Graph 2__: The following bar chart displays the top groups sold in cocouae per year and we notice how pants(women and men) is the most sold item and the least ones are accessories(socks and bags).
Look at the tooltips to understand how each parameter is impacting forecasts.
* __Graph 3__: We dig deeper in the third bar chart to see the sales distribtion per month and categories, exercise and style items are the most sold ones and overall the company sells the most in January and December.
* __Graph 4__: A pie chart shocasing the sales per store moreover the sales are the most in store c555 in all the years. \n
❗Select the year where you would like to explore the sales performance and the interactive average sales❗""")
    sales_product['Month'] = pd.DatetimeIndex(sales_product['Transaction Date'])
    sales_product['Month'] = sales_product['Month'].dt.month_name().str.slice(stop=3)
   # Filter the dataframe to 2000 so that it does not crash the browser
    sales_product_filtered = sales_product.sort_values(by='Net Amount', ascending=False).head(2000)
    #col1, col2, col3 = st.columns([3,3,1])
    year = st.sidebar.selectbox("Select a year",(sales_product.Year.unique()))
    from streamlit_extras.metric_cards import style_metric_cards
    avg_sales = np.mean(sales_product[sales_product['Year'] == year]['Net Amount'])
    avg_profit = np.mean(sales_product[sales_product['Year'] == year]['Net Gross Profit'])
    col1, col2, col3 = st.columns(3)
    with col1:
     col1.metric(label=f"Average Sales in {year}", value=round(avg_sales), delta=round(avg_sales)-80)
    with col2:
     col3.metric(label=f"Average Profit in {year}", value=round(avg_profit), delta=round(avg_profit)-80)
    #with col3:
     #col3.selectbox("Select a Year",(sales_product.Year.unique()), key='onlyone')
    style_metric_cards(border_left_color = '#8B8C8C')

    df_year=sales_product[sales_product['Year']==year]
    col1, col2, col3 = st.columns([5, 1, 4])

    with col1:
        #time series
            df_sales = df_year.groupby('Transaction Date')['Net Amount'].sum().reset_index()
            df_sales = df_sales.set_index('Transaction Date')
            fig4 = px.line(df_sales, x=df_sales.index, y='Net Amount', line_shape='linear')
            fig4.update_layout(
    title=f'Time-series graph representing Net Sales of cocouae in {year}',
    xaxis=dict(showgrid=False), 
    yaxis=dict(showgrid=True), 
    legend=dict(orientation='v'), 
    paper_bgcolor='#FFFFFF', 
    plot_bgcolor='#FFFFFF',  # set plot background color to white
    xaxis_rangeslider=dict(bgcolor='white'),  # set rangeslider background color

)   

            st.plotly_chart(fig4,use_container_width=True)
    with col3:
        df_year = df_year[df_year['Net Amount'] >=0]
        df_year2=df_year.groupby(['Group','Year']).agg(
    sales=('Net Amount', 'sum')
).sort_values(by='sales', ascending=False).reset_index()
        fig1 = px.bar(df_year2, x='Year', y='sales', color='Group')
        fig1.update_layout(
    title=f'Distribution of fashion groups in {year}', 
    xaxis = dict(
        showgrid=False, 
    ), 
    yaxis = dict(
        title='Sales', 
        showgrid=False
    ),
    legend = dict(
        orientation='v'
    ), 
    barmode='group', 
    paper_bgcolor='#FFFFFF'
)
            # set width and height of the plot
            #fig1.update_layout(width=1200, height=800)
        st.plotly_chart(fig1,use_container_width=True)

    col1, col2, col3 = st.columns([5, 1, 4])

    with col1:
            viz_df =sales_product.groupby(['Month','Year','Supp_Story'], as_index=False).agg(
            sales=('Net Amount', 'sum')
            ).sort_values(by='sales', ascending=False)
            viz_df = viz_df[viz_df['sales']>0]
            ordered_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"] #writing month in order since plotly uses alphabetical order
            viz_df['to_sort']=viz_df['Month'].apply(lambda x:ordered_months.index(x))
            viz_df = viz_df.sort_values('to_sort')
            fig3 = px.bar(viz_df[viz_df['Year'] == year],x='Month', y='sales',color='Supp_Story')
            fig3.update_layout(
    title=f'Monthly sales per category in {year}',
    xaxis = dict(
    	title='Month',
        showgrid=False, 
    ), 
    yaxis = dict(
        title='Sales', 
        showgrid=False
    ), 
    legend = dict(
        orientation='v'
    ),  
    paper_bgcolor='#FFFFFF'
)
            # set width and height of the plot
            #fig3.update_layout(width=1200, height=800)
            st.plotly_chart(fig3,use_container_width=True)


    with col3:
              fig2 = px.pie(sales_product[sales_product['Year'] == year], values='Net Amount', names='Store')
              fig2.update_layout(
     title=f'Sales per store in {year}',  
     yaxis = dict(
     ), 
     legend = dict(
        orientation='v'
     ), 
     barmode='group', 
     paper_bgcolor='#FFFFFF'
)
              st.plotly_chart(fig2,use_container_width=True)

with tab2:
    text = """
<h1 style="font-size: 24px;color:#c90515;text-align: center">
    <div style="display: inline-block">
        Budget vs Actual 
        <i class="far fa-question-circle" title="{txt}"></i>
    </div>
</h1>
"""

    txt = "We're going to analyze the profit behind the net sales"
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">', unsafe_allow_html=True)
    st.markdown(text.format(txt=txt), unsafe_allow_html=True)

    col1, col3, col2 = st.columns(([5, 1, 4]))
    with col1:
     #ith st.expander("Show charts", expanded=True):
        #ubcol1, subcol2,subcol3= st.columns([5, 1, 4])
        # Plot budget cost amount against fashionCOGS with OLS trendline
        fig1= px.scatter(Budget, x='FashionCOGS', y='Budget Margin Amount', trendline='ols', title='Budget Margin Amount vs FashionCOGS')
        col1.plotly_chart(fig1,use_container_width=True)
        Sales_Daily['Year'] = Sales_Daily['Transaction Date'].dt.year
        df_2022=Sales_Daily[(Sales_Daily['Year'] ==2022) & (Sales_Daily['Net Amount']>0)]
        fig2= px.scatter(df_2022, x='Net Cost Amount', y='Net Gross Profit', trendline='ols',title= "Actual Gross Profit vs Cost Amount")
        col2.plotly_chart(fig2,use_container_width=True)
    #with st.expander("Show correlation",expanded=True):

    col1.write(
   "As we can see in this section, Coco uae plans to get their profit margin from the cost of fashion sold and as the cost of fashion apparel **increases**, so should the profit margin."
)
    col2.write(
    "In the second line plot, we noticed that the relationship between net cost amount and net gross profit is weaker than planned however the increase is overall available but as a suggestion, Coco uae may need to **reduce** its costs to increase more their net gross profit."
)
        # Calculate the correlation matrix
    Budget_corr= Budget.corr()
    corr_matrix2 = df_2022[['Net Initial Price','Net Price','Net Cost Amount','Net Discount Amount','Net Amount','Net Gross Profit']].corr()
    # Define options for selectbox
    corr_options = {
    'Budget 2022 correlation': Budget_corr,
    'Actual 2022 correlation': corr_matrix2
}

# Show selectbox to choose correlation matrix
    corr_choice = st.selectbox("Explore correlation map between:", list(corr_options.keys()))

# Generate heatmap based on selected correlation matrix
    corr_matrix = corr_options[corr_choice]
    # Generate the heatmap using Plotly
    heatmap = go.Figure(data=go.Heatmap(
    z=corr_matrix.values,
    x=corr_matrix.columns,
    y=corr_matrix.index,
    colorscale='GnBu',
    colorbar=dict(title='Correlation'), 
))
# Add labels to the heatmap
    annotations = []
    for i, row in enumerate(corr_matrix.values):
            for j, value in enumerate(row):
               annotations.append(dict(
            x=corr_matrix.columns[j],
            y=corr_matrix.index[i],
            text=str(round(value, 2)),
            font=dict(color='white' if value > 0.95 else 'black'),
            showarrow=False
        )) 
    heatmap.update_layout(
    title='Correlation Heatmap',
    annotations=annotations
)
# Display the heatmap in the Streamlit app
    st.plotly_chart(heatmap,use_container_width=True)
