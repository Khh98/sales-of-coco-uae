import pandas as pd
from prophet import Prophet
#from prophet.make_holidays import get_holiday_names, make_holidays_df
import streamlit as st
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from prophet.plot import plot_plotly, plot_components_plotly
from streamlit_toggle import st_toggle_switch
from streamlit_extras.app_logo import add_logo
from streamlit_card import card

url1="https://drive.google.com/file/d/16vXzu_5wm5EhzgoOCnMRKmHMyIzez93_/view?usp=share_link"
klogo='https://drive.google.com/uc?export=download&id='+url1.split('/')[-2]


st.set_page_config(
     page_title="Analytical Tool",
     layout="wide",
     page_icon= klogo,
    initial_sidebar_state="expanded")

url1="https://drive.google.com/file/d/16vXzu_5wm5EhzgoOCnMRKmHMyIzez93_/view?usp=share_link"
klogo='https://drive.google.com/uc?export=download&id='+url1.split('/')[-2]


add_logo(klogo,height=130)

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
# Load and prepare the data
df = pd.read_csv('sales_df.csv')

# Load your holiday data into a dataframe
holidays_df = pd.read_csv('holidays.csv')

# Convert the holiday dates to datetime objects
holidays_df['date'] = pd.to_datetime(holidays_df['date'], format="%d/%m/%Y")
holidays_df = holidays_df.rename(columns={'date':'ds','Holiday':'holiday'})


expander = st.expander("Click me if you want to know more🙋🏻‍♂️")
expander.markdown("""Interpreting the Forecast Plot:

<ul>
  <li>The blue line represents the predicted values of the time series.</li>
  <li>The shaded blue area around the line represents the uncertainty around the predictions. The width of the shaded area represents the size of the confidence interval.</li>
  <li>The black dots represent the actual values of the time series, if available.</li>
  <li>If the predicted values closely match the actual values, the model is likely a good fit for the data. If there are significant discrepancies between the predicted and actual values, the model may not be a good fit.</li>
</ul>.""", unsafe_allow_html=True)
# Add an optional checkbox to enable/disable UAE holidays
enable_holidays = st_toggle_switch(
    label="Enable Holiday?",
    key="switch_1",
    default_value=False,
    label_after=False,
    inactive_color="#D3D3D3",  
    active_color="#11567f",  
    track_color="#29B5E8",  
)

# Filter holidays based on the checkbox value
if enable_holidays:
    holidays = holidays_df
else:
    holidays = None


text = """
<h1 style="font-size: 24px;color:#c90515;text-align: center">
    <div style="display: inline-block">
        Filters 
        <i class="far fa-question-circle" title="{txt}"></i>
    </div>
</h1>
"""

txt = "Interact to forecast sales per category for next 12 or 18 months and tune the model with params implemented here"
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">', unsafe_allow_html=True)
st.sidebar.markdown(text.format(txt=txt), unsafe_allow_html=True)

# Preprocess data
df = df[['Transaction Date', 'Category Name', 'Net Amount']]
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
df = df.groupby(['Category Name', pd.Grouper(key='Transaction Date', freq='M')]).sum().reset_index()
df.columns = ['category', 'ds', 'y']

#Get category input from user
category = st.sidebar.selectbox('Select Category:', df['category'].unique())
#get your season mode
mode = st.sidebar.selectbox('Seasonality mode:',['multiplicative','additive'])
# Create and fit model
model = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=False, seasonality_mode=mode,holidays=holidays)
# Set holiday parameters
# Assuming your holidays_df has 'ds' (date) and 'holiday' (event) columns
custom_holidays = holidays_df.rename(columns={'date': 'ds', 'Holiday': 'holiday'})

# Set holiday parameters in the Prophet model
if enable_holidays:
    model.add_country_holidays(country_name='AE')
    if custom_holidays is not None and not custom_holidays.empty:
        model.add_holidays(custom_holidays)



# Filter by selected category
df_category = df[df['category'] == category]

# Get forecast horizon input from user
forecast_horizon = st.sidebar.selectbox('Select forecast horizon (in months):', [12, 18])



# Get user input for hyperparameters
seasonality_prior_scale = st.sidebar.slider('Seasonality Prior Scale', min_value=0.1, max_value=100.0, value=10.0, step=0.1)
changepoint_prior_scale = st.sidebar.slider('Changepoint Prior Scale', min_value=0.001, max_value=10.0, value=0.05, step=0.001)

# Set hyperparameters
model.seasonality_prior_scale = seasonality_prior_scale
model.changepoint_prior_scale = changepoint_prior_scale
# Fit model to category data
model.fit(df_category)

# Generate future dates
future = model.make_future_dataframe(periods=forecast_horizon, freq='M')

# Generate forecasts
forecast = model.predict(future)

# Filter predictions for future dates only
forecast_future = forecast[['ds', 'yhat']].tail(forecast_horizon)

# Compute RMSE for the forecast
rmse = mean_squared_error(df_category['y'], forecast['yhat'][:len(df_category)]) ** 0.5

# Plot actual vs predicted values for past and future dates
fig1 = plot_plotly(model, forecast)
fig1.update_layout(title=f"Actual vs Predicted Net Amount ({category} - Past and Future Dates)")
st.plotly_chart(fig1)

# Plot Prophet components for past and future dates
fig2 = plot_components_plotly(model, forecast)
fig2.update_layout(title=f"Prophet Components ({category} - Past and Future Dates)")
st.plotly_chart(fig2)
# Display RMSE
if enable_holidays:
    card(title=f"RMSE ({category} with UAE Holidays)",text=round(rmse,2),url="https://www.statisticshowto.com/probability-and-statistics/regression-analysis/rmse-root-mean-square-error/")
else:
    card(title=f"RMSE ({category} without UAE Holidays)",text=round(rmse,2),url="https://www.statisticshowto.com/probability-and-statistics/regression-analysis/rmse-root-mean-square-error/")
