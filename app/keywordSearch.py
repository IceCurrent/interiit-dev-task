import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

apiKey = os.environ.get("NEWS_API_KEY")

def searchKeywords(keywords, sortby):

    if sortby and keywords:
        return f"https://newsapi.org/v2/everything?q={keywords}&language=en&pageSize=20&sortBy={sortby}&apiKey={apiKey}"
    
    elif keywords:
        return f"https://newsapi.org/v2/everything?q={keywords}&language=en&pageSize=20&apiKey={apiKey}"

    else:
        return f"https://newsapi.org/v2/top-headlines?language=en&apiKey={apiKey}"
