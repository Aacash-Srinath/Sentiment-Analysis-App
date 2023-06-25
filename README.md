# Sentiment Analysis App
### Web App to Calculate the Sentiment Rating of any Comment or the Average Sentiment Rating of the Reviews of any Amazon Product

Files:
- scrapeAmazon.py
- sentimentRating.py
- sentiment-app.py

____

#### 1. scrapeAmazon.py
- Uses a the Selenium Library in Python to Web Scrape Reviews of Products from amazon.in
- Products are Identified Using the ASIN Value (Amazon Serial Identification Number)
- Scrapes All the Reviews of the Product (If Available) and Compiles it into a Dataframe
- Returns the DataFrame
____

#### 2. sentimentRating.py
- Uses a Pre-Trained BERT Model and Tokenizer from the Transformers library to perform Sentiment Analysis on a Given Text
- Returns the Sentiment Rating as the Output
____

> sentiment-app.py
- Python Script for Running the Streamlit App
- Contains a Dropdown Box to Choose between Sentiment Analysis of a Text/Comment and Amazon Product Reviews
  ![image](https://github.com/Aacash-Srinath/Sentiment-Analysis-App/assets/100955640/d3681f9c-ca04-4121-9964-7a55b4b2c4c2)
  - For Text/Comment: Returns the Sentiment Rating of the Comment
  - For Amazon Product Reviews: Returns the Mean Sentiment Rating of All Reviews Available (Reviews from India Only)
