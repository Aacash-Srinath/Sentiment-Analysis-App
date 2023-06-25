import streamlit as st
import pandas as pd
import numpy as np
import sentimentRating

# Streamlit Page Configurations
st.set_page_config(page_title="Sentiment Analysis | Aacash Srinath",
                   page_icon=None,
                   initial_sidebar_state="collapsed",
                   menu_items=None)

# Page Title & Subheading
st.title("Sentiment Analysis for Text")
st.subheader("Web App to Predict the Sentiment of a Comment")

st.write("")
st.write("")

comment = st.text_input("# **Enter Comment**")
rating = 0
if (comment):
    rating = sentimentRating.sentimentRating(comment)
    st.write('')
    st.markdown(f"<h3 style='text-align: center;'>The Sentiment Rating of the Comment is {rating} </h3>", unsafe_allow_html=True)
