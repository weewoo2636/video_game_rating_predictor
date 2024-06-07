# import libraries
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


@st.cache_data
def load_data():
    df = pd.read_csv('cleaned.csv')
    return df


def app():
    st.title('Exploratory Data Analysis')
    st.write('---')

    data_load_state = st.text('Loading data...')
    df = load_data()
    data_load_state.text("Done!")

    st.subheader('Dataset Preview')
    st.write(df)

    st.subheader('**Data Analysis Questions**')
    st.write('---')

    st.write('### **1. How is the data distribution of rating?**')
    st.write('''
             - Insight:
                - Rating data is `normally distributed` since our absolute skewness is not greater than 0.5
             ''')
    image = Image.open('eda_1.png')
    st.image(image)

    st.write('### **2. What is the correlation between estimated_total_players and rating?**')
    st.write('''
             - **Note:**
                - Because our data doesn't inform us about the total_player, we'll get the data by estimating total_player by the formula provided [here](https://www.themultiplayergroup.com/news/using-steam-reviews-to-estimate-player-numbers-an-intuitive-method)
                - The correlation coefficient that we'll use is spearman because our 2 variables are numeric and not normally distributed
            - **Insight:**
                - estimated_total_player and rating are `positively correlated` (an increase in estimated_total_player would be followed by an increase in rating)
                    - The correlation is `by real` (p-value: 0.00 which is less than 0.05 based on 95% confidence level) 
             ''')
    image = Image.open('eda_2.png')
    st.image(image)

    st.write('### **3. What are the top 3 genres, tags, features, languages with the highest average rating?**')
    st.write('''
             - **Insight:**
                - Based on the rating,
                    - the top 3 genres are `Design`, `Free`, `Adventure`
                    - the top 3 tags are `Birds`, `SteamMachine`, `Well-Written`
                    - the top 3 features are `DownloadableContent`, `Mods`, `RemotePlayOnTablet`
                    - the top 3 languages are `Portugese-Brazil`, `Japanese`, `Korean` 
             ''')
    image = Image.open('eda_3.png')
    st.image(image)

    st.write('### **4. How is the central tendency of price for games with either top 3 genres, tags, features, or languages?**')
    st.write('''
             - **Insight:**
                - The central tendency of price for games with either top 3 games, tags, features, or languages are,
                    - mean: `67.82`
                    - median: `69.20`
                    - mode: `50.00`
             ''')
    image = Image.open('eda_4.png')
    st.image(image)

    st.write('### **5. What is the average estimated_total_players of each rating category?**')
    st.write('''
             - **Note:**
                - Rules on rating category following [source](https://steamcommunity.com/discussions/forum/0/1744482869761322402/) are as such, 

            |%score  |   #reviews   |  rating  |   confidence
            |---|---|---|---|
            |95 - 100 | 500+ reviews | positive | overwhelmingly
            |85 - 100 |  50+ reviews | positive | very
            |80 - 100 |  10+ reviews | positive | -
            |70 -  79 |  10+ reviews | positive | mostly
            |40 -  69 |  10+ reviews | mixed    | -
            |20 -  39 |  10+ reviews | negative | mostly
            | 0 -  19 |  10+ reviews | negative | -
            | 0 -  19 |  50+ reviews | negative | very
            | 0 -  19 | 500+ reviews | negative | overwhelmingly

            - **Insight:**
                - There is a significant increase in estimated total players after rating category goes beyond mixed (positive and above)
                - The average estimated total players of each rating category are as such,

            |rating_category|estimated_total_players|
            |---|---|
            |overwhelmingly_negative |36985|
            |very_negative |10680|
            |negative |570|
            |mostly_negative |12587|
            |mixed |18761|
            |mostly_positive |32062|
            |positive |86524|
            |very_positive |431295|
            |overwhelmingly_positive |3323016|
             
             ''')
    image = Image.open('eda_5.png')
    st.image(image)

    st.write('### **6. How does average rating changes as the amount of supported languages increases?**')
    st.write('''
             - **Insight:**
                - Generally, the average rating `barely increases` as the amount of supported languages increases
                - There is a `diminishing return` in rating when the amount of supported languages goes past beyond 10
             ''')
    image = Image.open('eda_6.png')
    st.image(image)

    st.write('### **7. How does average rating changes as the amount of current players increase?**')
    st.write('''
             - **Note:**
                - To make the chart easier to read, we'll group the current players into groups that follows these rules,
                    - `<500`
                    - `500 - 999`, `1000 - 1999`, `2000 - 2999`, `3000 - 3999`, `4000 - 4999`, `5000 - 2599`, `6000 - 6999`, `7000 - 7999`, `8000 - 8999`, `9000 - 9999`
                    - `10000+`
            - **Insight:**
                - Generally, the average rating `barely increases` as the amount of current players increase
                - There is a `diminishing return` in rating when the amount of current players goes past beyond 10_000
             ''')
    image = Image.open('eda_7.png')
    st.image(image)



