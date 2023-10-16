import streamlit as st
import requests
from keywordSearch import searchKeywords
from headlineSearch import headlines
from emaildb import users


st.set_page_config(page_title="Hooly News", page_icon="🔞", layout="wide")

st.title("Hooly News")

# Create a newsletter subscription section at the top-right
st.sidebar.markdown("### Subscribe to our newsletter")
email = st.sidebar.text_input("Enter your email")
subscribeButton = st.sidebar.button("Subscribe")

if subscribeButton:

    if(users.find_one({"email": email})):
       st.success("You have already subscribed!")
    else:
        users.insert_one({"email": email})
        st.success("Thank you for subscribing")


main_tab = st.sidebar.selectbox("Select a section", ("Top Headlines", "Search for News"))

def display_article(article):
    title = article.get("title")
    published_at = article.get("publishedAt")
    source = article.get("source", {}).get("name")
    author = article.get("author")
    description = article.get("description")
    content = article.get("content")
    reference = article.get("url")
    img = article.get("urlToImage")

    st.markdown("---")

    if title:
        st.markdown(f"**{title}**")
    if published_at:
        st.markdown(f"Published at: {published_at}")
    if source:
        st.markdown(f"Source: {source}")
    if author:
        st.markdown(f"Author: {author}")
    if content:
        st.markdown(content)
    if reference:
        st.write(reference)
    if img:
        st.image(img, use_column_width=True)


if main_tab == "Top Headlines":
    country = st.sidebar.text_input("Enter the country")
    category = st.sidebar.selectbox("Select a category", ("sports", "business", "technology", "health", "science", "entertainment"))

    top_headlines_url = headlines(country=country, category=category)
    r = requests.get(url=top_headlines_url)
    r = r.json()

    articles = r['articles']

    if not articles:
        st.error("Couldn't fetch top headlines.")
    else:
        for article in articles:
            display_article(article)

else:
    # Create a sub-tab for "Search" within the "Search for News" section
    # search_tab = st.sidebar.selectbox("Select a tab", ("Keyword Search"))

    keywords = st.sidebar.text_input("Enter keywords")
    sortby = st.sidebar.selectbox("Sort by", ("relevancy", "popularity", "publishedAt"))

    # Check if keywords are not empty and a search is requested
    # if st.button("Search") and keywords:
        # Make API call for keyword search
    search_url = searchKeywords(keywords=keywords, sortby=sortby)
    r = requests.get(url=search_url)
    r = r.json()

    articles = r['articles']

    if not articles:
        st.error("Couldn't fetch articles.")
    else:
        for article in articles:
            display_article(article)


