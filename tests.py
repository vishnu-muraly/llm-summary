
import json
import requests
from newspaper import Article
from bs4 import BeautifulSoup

headers_ = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

article_url = "https://thehackernews.com/2023/07/mexico-based-hacker-targets-global.html"

session = requests.Session()

response_ = session.get(article_url, headers=headers_, timeout=10)

if response_.status_code == 200:
    try:
        article = Article(article_url)
        article.download()
        article.parse()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(article.html, 'html.parser')
        # Extract the text from the HTML content
        text = soup.get_text(separator=' ')

        print(f"Title: {article.title}")
        #print(f"Text: {text}")
    except Exception as e:
        print("Error while parsing the article:", e)
else:
    print("Error while fetching the article, please check the URL...")






