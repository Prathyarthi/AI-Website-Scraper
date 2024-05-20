import streamlit as st
from scrape import scrape_website

st.title("AI WEB SCRAPER")
url = st.text_input("Enter a website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping site...")
    result = scrape_website(url)
    print(result)

