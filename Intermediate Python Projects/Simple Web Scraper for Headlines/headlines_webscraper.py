# 16. Simple Web Scraper for Headlines   
#     *Description*: Create a basic web scraper that extracts headlines from a news website.  
#     *Skills*: Basic HTML parsing with BeautifulSoup, making HTTP requests.


import requests
from bs4 import BeautifulSoup

news_url = "https://kathmandupost.com/"

response = requests.get(news_url)

if response.status_code == 200:
    print("Successfully fetched the page!")
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    headlines = soup.find_all('h2')
    
    print("Here are the latest headlines:")
    for i, h2 in enumerate(headlines, 1):
        a_tag = h2.find('a')  
        if a_tag:
            headline_text = a_tag.get_text()  
            print(f"{i}. {headline_text}")
else:
    print(f"Failed to fetch the page. Status Code:{response.status_code}")
    

