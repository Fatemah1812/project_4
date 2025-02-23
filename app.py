import streamlit as st
import pandas as pd 
import plotly.express as px
import plotly.io as pio

vehicles=pd.read_csv('vehicles_us (1).csv')
st.header('USA Vehicals Data analysis')

cars_days_listed=vehicles.groupby('type')['days_listed'].mean().reset_index()
st.header('Car Types vs Average days cars are listed')
plot=px.scatter(cars_days_listed, x="type", y="days_listed", 
                 title="Car Types vs Average days cars are listed ",
                 labels={ 'days_listed': 'Average days cars are listed'}
                 )

if st.checkbox('Show Histogram'):
        st.plotly_chart(plot)
                 
car_prices_fuel=vehicles[['fuel','price']]
st.header('Distribution of Price by Fuel Type')
hist=px.histogram(car_prices_fuel, x='price', color='fuel', 
                 title='Distribution of Price by Fuel Type',
                 labels={'price': 'Price (USD)', 'fuel': 'Fuel Type'})

if st.checkbox('Show Histogram'):
        st.plotly_chart(hist)