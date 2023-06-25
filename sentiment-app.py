import streamlit as st
import pandas as pd
import numpy as np

import sentimentRating
import scrapeAmazon

# Streamlit Page Configurations
st.set_page_config(page_title="Sentiment Analysis | Aacash Srinath",
                   page_icon=None, layout="wide",
                   initial_sidebar_state="collapsed",
                   menu_items=None)

# Page Title & Subheading
st.title("Sentiment Analysis for Text & Amazon Product Reviews")
st.subheader("Web App to Predict the Sentiment of Comment/Amazon Product Reviews")

# Dropdown Box to Choose
st.write("")
st.write("")
choice = st.selectbox(' **Sentiment Analysis Of** ',['Choose', 'Comment', 'Amazon Product Reviews (India Only)'])
st.write("")
st.write("")

# If Comment is Selected from the Dropdown Box
if (choice == 'Comment'):
    comment = st.text_input("**Enter Comment**")
    rating = 0
    if (comment):
        rating = sentimentRating.sentimentRating(comment)
        st.write('')
        st.markdown(f"<h3 style='text-align: center;'>The Sentiment Rating of the Comment is {rating} </h3>", unsafe_allow_html=True)

# If Amazon Product Review is Selected from the Dropdown Box
if (choice == 'Amazon Product Reviews (India Only)'):
    view = False
    asin_val = st.text_input("**Enter Amazon Standard Identification Number (ASIN)**")
    if (asin_val):
        reviewDF = scrapeAmazon.getReviews(asin_val)
        reviewsArray = reviewDF['review'].to_numpy()

        sentiment = []
        for review in reviewsArray:
            rating = (sentimentRating.sentimentRating(review))
            sentiment.append(rating)
        s = pd.Series(sentiment)
        reviewDF['rating'] = s

        avgRating = round(reviewDF['rating'].mean(), 2)
        st.write('')
        st.markdown(f"<h3 style='text-align: center;'>The Average Sentiment Rating of the Product is {avgRating} </h3>", unsafe_allow_html=True)
