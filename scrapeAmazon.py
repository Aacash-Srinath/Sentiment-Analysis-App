import pandas as pd
import streamlit as st
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def getReviews(asin):
    # Set up the web driver
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    driver = get_driver()

    # Navigate to the product page
    product_url = f"https://www.amazon.in/dp/{asin}"
    driver.get(product_url)

    # Click on the "See all reviews" link
    try:
        #WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.ID, "reviews-medley-footer")))
        see_all_reviews_link = driver.find_element(By.XPATH, "//*[@id='reviews-medley-footer']/div[2]/a")
        see_all_reviews_link.click()
    except:
        st.write("**No Reviews To Analyse From India**")
        sys.exit(1)
    
    reviewList = []

    # Wait for the reviews section to load
    WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.ID, "cm_cr-review_list")))

    #Scroll to the bottom of the page to load all reviews (you may need to adjust the sleep time based on your internet speed)
    while True:
        # Scrape all the reviews on the current page
        reviews = driver.find_elements(By.XPATH, "//div[@data-hook='review']")
        for review in reviews:
            try:
                review1 = {}
                # Extract relevant information from each review element
                rating = review.find_element(By.CSS_SELECTOR, ".review-rating span").get_attribute("innerHTML")
                title = review.find_element(By.CSS_SELECTOR, ".review-title").get_attribute("innerHTML")
                title = title.split("<span>")[1].split("</span")[0]
                content = review.find_element(By.CSS_SELECTOR, ".review-text span").get_attribute("innerHTML")
                
                # Store the extracted information as per your requirements
                review1 = {'title':title, 'review':content}
                reviewList.append(review1)
            except:
                pass

        #Check if there is a next page button
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, ".a-pagination .a-last a")
        except:
            break

        # Click the next page button and wait for the new page to load
        try:
            next_button.click()
            WebDriverWait(driver, 20).until(EC.staleness_of(reviews[0]))
        except:
            pass

    data = pd.DataFrame(reviewList)
    return data
