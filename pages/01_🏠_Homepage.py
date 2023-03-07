import streamlit as st 
from streamlit_lottie import st_lottie
from streamlit_extras.echo_expander import echo_expander
from streamlit_extras.app_logo import add_logo
import pandas as pd
import requests
import streamlit as st

url1="https://drive.google.com/file/d/12NQM8wBzIl3XwJqAGLZnZ3r3El9A6hyq/view?usp=sharing"
pacclogo='https://drive.google.com/uc?export=download&id='+url1.split('/')[-2]

st.set_page_config(
     page_title="Analytical Tool",
     layout="wide",
     page_icon= pacclogo,
    initial_sidebar_state="expanded")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



url1="https://drive.google.com/file/d/12NQM8wBzIl3XwJqAGLZnZ3r3El9A6hyq/view?usp=sharing"
pacclogo='https://drive.google.com/uc?export=download&id='+url1.split('/')[-2]


add_logo(pacclogo,height=200)


# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_ipbqqshx.json")

#LOAD DATASETS
#function to read large data with caching
@st.cache_data()
def load_data(path):
    df=pd.read_csv(path)
    return df


#read the 2nd dataframe
url2 = 'https://drive.google.com/file/d/1KlN6GLxMRJ2cyS057vl3E2l1BfxoaG0R/view?usp=sharing'
path2 = 'https://drive.google.com/uc?export=download&id='+url2.split('/')[-2]
Sales_Daily=load_data(path2)


# Imported Product.csv
Product = pd.read_csv('Product.csv')


# Imported Stock.csv
#read the 2nd dataframe
url3 = 'https://drive.google.com/file/d/1hB2xOLcbPP4P-zZmidcLWBUEfcD4TJlX/view?usp=sharing'
path3 = 'https://drive.google.com/uc?export=download&id='+url3.split('/')[-2]
Stock=load_data(path3)

# Imported Holidays_By_Country.csv
Holidays_By_Country = pd.read_csv('Holidays_By_Country.csv')

# Imported Budget.csv
Budget = pd.read_csv('Budget.csv')

# Changed Date to dtype datetime
Budget['Date'] = pd.to_datetime(Budget['Date'], format='%d/%m/%Y', errors='coerce')

# Sorted Date in ascending order
Budget = Budget.sort_values(by='Date', ascending=True, na_position='first')

# Changed Fromdate, To_Date to dtype datetime
Stock['Fromdate'] = pd.to_datetime(Stock['Fromdate'], infer_datetime_format=True, errors='coerce')
Stock['To_Date'] = pd.to_datetime(Stock['To_Date'], format='%d/%m/%Y', errors='coerce')

# Changed Transaction Date to dtype datetime
Sales_Daily['Transaction Date'] = pd.to_datetime(Sales_Daily['Transaction Date'], format='%d/%m/%Y', errors='coerce')

# Sorted Transaction Date in ascending order
Sales_Daily = Sales_Daily.sort_values(by='Transaction Date', ascending=True, na_position='first')

# Sorted Transaction Date in ascending order
Sales_Daily = Sales_Daily.sort_values(by='Transaction Date', ascending=True, na_position='first')

# Changed OriginalPrice to dtype float
Product['OriginalPrice'] = pd.to_numeric(Product['OriginalPrice'], errors='coerce')

# Deleted columns Category, MODIFIEDDATETIME, Item Creation Date, Supp_BrandL2, Supp_BrandL4, Supp_Fabric
Product.drop(['Category', 'MODIFIEDDATETIME', 'Item Creation Date', 'Supp_BrandL2', 'Supp_BrandL4', 'Supp_Fabric'], axis=1, inplace=True)

# Deleted columns Width, Product Type, Height
Product.drop(['Width', 'Product Type', 'Height'], axis=1, inplace=True)


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




st.text("")
st.text("")
html ="<h1 style='text-align: center;font-size: 52px'>Showcasing The Power Of Analytics</h1>"
st.markdown(html, unsafe_allow_html=True)
st.text("")
st.text("")


html = '''
    <h1 style="font-size: 24px;background-color:#c90515;color:White;text-align: center">Home</h1>
    '''
st.markdown(html, unsafe_allow_html=True)


st.write("")
st.write("")

col1, col2, col3 = st.columns([1,7,1])
with col2:
        html="""<h3 style="font-size:25px;line-height:1.5em;"> With the goal of unlocking <b><span style="color: #c90515;">the full potential of sales analytics</span></b>, this project focuses on utilizing advanced tools and techniques to analyze the sales data of Cocouae company and gain a deeper understanding of its sales performance and spur business growth.<br>This web app aims to <span style="color: #c90515;">analyze, explore and forecast</span> past and current sales</br></h3>"""
        st.markdown(html, unsafe_allow_html=True)

st.write("")
st.write("")


col1, col2, col3 = st.columns([1,5,1])
with col2:
        st_lottie(lottie_coding, height=250, key="coding")

st.write("")
    # st.write("")

html2 = '''
    <h3 style="font-size:25px;line-height:1.5em;"><b>Kindly expand the arrow down to start exploring right-away the data</b></h3>


    '''

dataframes = {
    "Product": Product,
    "Sales_Daily": Sales_Daily,
    "Stock": Stock,
    "Holidays_By_Country": Holidays_By_Country,
    "Budget": Budget
}
col1, col2, col3 = st.columns([1,7,1])
with col2:
        st.markdown(html2, unsafe_allow_html=True)
        st.write("")
        with echo_expander(code_location="below", label="Sneak peeck of the code😜"):
            datasets = ["Product", "Daily Sales", "Stock", "Holidays by Country", "Budget"]
            dataset_descriptions = [    "The product dataset contains information about the products that the company sells, including product key, brand, category, and vendor information.",    "The daily sales dataset contains information about the client transactions that occur in the company's stores on a daily basis.",    "The stock dataset contains information about the quantity of stock that is available in the company's stores for specific products.",    "The holiday dataset contains data about the day-offs in each country.",    "The budget dataset contains information about the budgeted sales, margin, cost, and fashion COGS for a company."]
            for dataset, description in zip(datasets, dataset_descriptions):
                 st.markdown(f"### {dataset}")
                 st.markdown(description)

        # Show Dataset
        st.write("")
        if st.checkbox("Show Dataset"):
         number = st.number_input("Numbers of rows to view", 5)
         df_name = st.selectbox("Select a dataframe", list(dataframes.keys()))
         df_select = dataframes[df_name]
         st.dataframe(df_select.head(number))


