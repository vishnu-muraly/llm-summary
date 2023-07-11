import streamlit as st
import json
import requests
import time
from newspaper import Article


# Page title layout
c1, c2 = st.columns([0.32, 2])

with c1:
     st.image("images/newspaper.png", width=85)

with c2:
    st.title("FastNews Article Summarizer")

st.markdown("**Generate summaries of online articles using abstractive summarization with Google's PEGASUS model.**")


# Sidebar content
st.sidebar.subheader("About the app")
st.sidebar.info("This app uses 🤗HuggingFace's [google/pegasus-cnn_dailymail](https://huggingface.co/google/pegasus-cnn_dailymail) model.\
                 \nYou can find the source code [here](https://github.com/ivnlee/streamlit-text-summarizer)")
st.sidebar.write("\n\n")
st.sidebar.markdown("**Get a free API key from HuggingFace:**")
st.sidebar.markdown("* Create a [free account](https://huggingface.co/join) or [login](https://huggingface.co/login)")
st.sidebar.markdown("* Go to **Settings** and then **Access Tokens**")
st.sidebar.markdown("* Create a new Token (select 'read' role)")
st.sidebar.markdown("* Paste your API key in the text box")
st.sidebar.divider()
st.sidebar.write("Please make sure your article is in English and is not behind a paywall.")
st.sidebar.write("\n\n")
st.sidebar.divider()
st.sidebar.caption("Created by [Ivan Lee](https://ivan-lee.medium.com/) using [Streamlit](https://streamlit.io/)🎈.")


# Inputs 
st.subheader("Enter the URL of the article you want to summarize")
default_url = "https://"
url = st.text_input("URL:", default_url)

headers_ = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }

fetch_button = st.button("Fetch article")

if fetch_button:
    article_url = url
    session = requests.Session()

    try:
        response_ = session.get(article_url, headers=headers_, timeout=10)
    
        if response_.status_code == 200:

            with st.spinner('Fetching your article...'):
                time.sleep(3)
                st.success('Your article is ready for summarization!')

        else:
            st.write("Error occurred while fetching article.")

    except Exception as e:
        st.write(f"Error occurred while fetching article: {e}")


# HuggingFace API KEY input
API_KEY = st.text_input("Enter your HuggingFace API key", type="password")

# HuggingFace API inference URL.
API_URL = "https://api-inference.huggingface.co/models/google/pegasus-cnn_dailymail"

headers = {"Authorization": f"Bearer {API_KEY}"}


submit_button = st.button("Submit")

# Download and parse the article
if submit_button:
    article = Article(url)
    article.download()
    article.parse()

    title = article.title
    text = article.text

    # HuggingFace API request function
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    
    with st.spinner('Doing some AI magic, please wait...'):
        time.sleep(1)

        # Query the API
        output = query({"inputs": text, })

       # Display the results
        summary = output[0]['summary_text'].replace('<n>', " ") 

        st.divider()
        st.subheader("Summary")
        st.write(f"Your article: **{title}**")
        st.write(f"**{summary}**")