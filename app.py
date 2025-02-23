import streamlit as st
import pandas as pd 
import plotly.express as px
import plotly.io as pio

vehicles=pd.read_csv('vehicles_us (1).csv')
st.header('USA Vehicals Data analysis')

vehicles['model_year'] = vehicles['model_year'].fillna(vehicles['model_year'].median())

vehicles['cylinders'] = vehicles.groupby('model')['cylinders'].fillna(vehicles['cylinders'].median())

vehicles['odometer'] = vehicles.groupby('model')['odometer'].fillna(vehicles['odometer'].median())

cars_days_listed=vehicles.groupby('odometere')['days_listed'].mean().reset_index()
st.header('Car Milage vs Car Demand')

plot=px.scatter(cars_days_listed, x="odometer", y="days_listed", 
                 title="Car Milage vs Average days cars are listed ",
                 labels={ 'days_listed': 'Average days cars are listed'}
                 
                 )

if st.checkbox('Show Plot'):
        st.plotly_chart(plot)

                 
car_prices_fuel=vehicles[['fuel','price']]
st.header('Distribution of Price by Fuel Type')

hist=px.histogram(car_prices_fuel, x='price', color='fuel', 
                 title='Distribution of Price by Fuel Type',
                 labels={'price': 'Price (USD)', 'fuel': 'Fuel Type'}
                 )

if st.checkbox('Show Histogram'):
        st.plotly_chart(hist)