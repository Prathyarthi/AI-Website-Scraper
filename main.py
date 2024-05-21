import streamlit as st
from scrape import scrape_website, extract_body_content,clean_body_content,split_dom_content

st.title("AI WEB SCRAPER")
url = st.text_input("Enter a website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping site...")
    result = scrape_website(url)

    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("Show DOM Content"):
        st.text_area("DOM content",cleaned_content,height=300)

