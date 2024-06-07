# import libraries
import streamlit as st
import numpy as np
import pandas as pd
import joblib


@st.cache_data
def load_data():
    df = pd.read_csv('cleaned.csv')
    return df


def app():
    st.title('Prediction for Game Rating')
    st.write('---')

    data_load_state = st.text('Loading data...')
    df = load_data()
    data_load_state.text("Done!")
    
    st.subheader('Dataset Preview')
    st.write(df)

    st.subheader('Input Data')
    st.write('---')
    input = user_input(df)

    st.subheader('User Input')
    st.write(input)

    load_pipeline = joblib.load("regressor_pipeline.pkl")
    prediction = load_pipeline.predict(input)

    st.subheader('Prediction Result:')
    st.write('Based on user input, the model predicted the rating of the game is: ')
    st.write(prediction)

def user_input(df):
    primary_genre = st.selectbox('primary_genre', df['primary_genre'].unique())
    players_right_now = st.number_input('players_right_now', value=0)
    _24_hour_peak = st.number_input('24_hour_peak', value=0)
    original_price = st.number_input('original_price', value=0.0)

    data = {
        'primary_genre' : primary_genre,
        'players_right_now' : players_right_now,
        '24_hour_peak' : _24_hour_peak,
        'original_price': original_price
    }
    features = pd.DataFrame(data, index=[0])
    return features


