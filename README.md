# Sentiment Analysis App
### Web App to Calculate the Sentiment Rating of any Comment or the Average Sentiment Rating of the Reviews of any Amazon Product

Files:
- scrapeAmazon.py
- sentimentRating.py
- sentiment-app.py

> scrapeAmazon.py
> - Script for Scraping Reviews of a Product in amazon.in
> - Requires Product ASIN Value (Amazon Serial Identification Number)
> - Outputs the Title and Content of Reviews as a DataFrame

> sentimentRating.py
> - Contains the function **sentimentRating(review)**
> - Requires Text as Parameter
> - Calculates Sentiment Rating of Given Text
> - Outputs the Rating of the Given Text

> sentiment-app.py
> - Python Script for Running the Streamlit App
> - Contains a Dropdown Box to Choose between Sentiment Analysis of a Text/Comment and Amazon Product Reviews
>   - For Text/Comment: Returns the Sentiment Rating of the Comment
>   - For Amazon Product Reviews: Returns the Mean Sentiment Rating of All Reviews Available (Reviews from India Only)
