import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

def scrape_website(website):
    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Page Loaded!")

        html = driver.page_source
        time.sleep(10)
        return html
    
    finally:
        driver.quit()

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content,"html.parser")
    body_content = soup.body

    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content,"html.parser")

    for scripts_styles in soup(["script", "style"]):
        scripts_styles.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())  # Removing extra \n characters which are not actually separating anything or any spaces.

    return cleaned_content

def split_dom_content(dom_content,max_length=6000):
    return [
        dom_content[i:i+max_length] for i in range(0,len(dom_content),max_length) # Splitting the content into chunks of 6000 characters. The for loop explain that it starts from 0 and goes upto the length of the content and step-size is 6000.
    ]
