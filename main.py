import streamlit as st
import json
import requests
#import sentencepiece
from transformers import pipeline
from newspaper import Article


header = st.container()
inputs = st.container()
outputs = st.container()


with header:
    st.title("Article Summarizer app")
    st.markdown("#### This app summarizes web articles using HuggingFace's transformers library")

with inputs: 
    st.subheader("Enter the URL of the article you want to summarize")
    url = st.text_input("URL:")
    st.divider()

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }

    article_url = url
    session = requests.Session()

    try:
        response = session.get(article_url, headers=headers, timeout=10)

        if response.status_code == 200:
            article = Article(article_url)
            article.download()
            article.parse()
        
        else:
            st.write("Failed to fetch article from URL")

    except Exception as e:
        st.write("Failed to fetch article, please check the URL again.") 

