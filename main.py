import streamlit as st
import json
import requests
from newspaper import Article

# Page layout
st.title("Article Summarizer app")
st.markdown("#### This app summarizes web articles using HuggingFace's transformers library")

# inputs: 
st.subheader("Enter the URL of the article you want to summarize")
default_url = "https://thehackernews.com/2023/07/mexico-based-hacker-targets-global.html"
url = st.text_input("URL:", default_url)
st.divider()


headers_ = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }

article_url = url
session = requests.Session()

response_ = session.get(article_url, headers=headers_, timeout=10)

if response_.status_code == 200:
    article = Article(article_url)
    article.download()
    article.parse()

    title = article.title
    text = article.text

else:
    st.write("Error while fetching the article, please check URL...")

# HuggingFace API KEY
API_KEY = st.text_input("Enter your HuggingFace API key", type="password")

# HuggingFace API inference URL.
API_URL = "https://api-inference.huggingface.co/models/google/pegasus-cnn_dailymail"
headers = {"Authorization": f"Bearer {API_KEY}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
  
output = query({"inputs": text, })

st.divider()
st.subheader("Summary")
st.write(title)
st.write(output)
