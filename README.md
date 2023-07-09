
# 📰 FastNews Article Summarizer

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://article-summarizer-app.streamlit.app) 👈🏻 Give it a try!


### Generate summaries of news articles or blog posts using Google's language model Pegasus via 🤗 HuggingFace's API. 

Pegasus is an encoder-decoder style transformer, specifically trained for abstractive summarization tasks. For this app I used the checkpoint: [google/pegasus-cnn_dailymail](https://huggingface.co/google/pegasus-cnn_dailymail), trained on the CNN-Dailymail corpus.

*For more information about the model, see the original paper [PEGASUS: Pre-training with Extracted Gap-sentences for Abstractive Summarization](https://arxiv.org/pdf/1912.08777.pdf) by Jingqing Zhang, Yao Zhao, Mohammad Saleh and Peter J. Liu, published on Dec 18, 2019.*

## About this app

You will need an API key from **HuggingFace**. In case don't have one already, follow these steps:
- Create a [free account](https://huggingface.co/join) or [login](https://huggingface.co/login)
- Go to **Settings** and then **Access Tokens**
- Create a new Token (select 'read' role)
- Paste your API key in the app's text box

<img width="1552" alt="summarizer-app" src="https://github.com/ivnlee/streamlit-text-summarizer/assets/104610424/3a82334d-fd5d-47a2-8498-02259dd6dd0a">


**Considerations:**
- The model works best with articles in English
- Articles behind paywall restrictions can't be accessed
- Longer articles require more processing time and resources
- It may not be possible to scrape some websites
