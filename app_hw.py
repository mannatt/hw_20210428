#//////////////////////////////////app.py file

import streamlit as st 
import pandas as pd
import plotly.express as px

@st.cache
def load_data():
    data = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/nationalcasedeath/csv')
    data['week'] = data.year_week.apply(lambda x: convert(x))
    return data

def convert(x):
    year, week = x.split('-')
    year = (int(year) - 2020) * 54 
    return year + int(week)

data = load_data()

fig = px.line(data_frame = data, x = 'week', y = 'cumulative_count', color = 'indicator', )

st.title("Covid cases")
country = st.sidebar.selectbox('Select a country', data['country'])
st.write(f'The selected country is {country}')
st.plotly_chart(fig)



