import streamlit as st
import pycountry 
from dotenv import load_dotenv
import os

load_dotenv()

apiKey = os.environ.get("NEWS_API_KEY")

def headlines(country, category):
    if category and country:
        cntry = pycountry.countries.get(name=country)
        if cntry is None:
            st.error("Invalid country name")
        else:
            country_code = cntry.alpha_2

        return f"https://newsapi.org/v2/top-headlines?country={country_code}&language=en&category={category}&apiKey={apiKey}"
    
    elif category:
        return f"https://newsapi.org/v2/top-headlines?category={category}&language=en&apiKey={apiKey}"
    
    elif country:
        cntry = pycountry.countries.get(name=country)
        if cntry is None:
            st.error("Invalid country name")
        else:
            country_code = cntry.alpha_2

        return f"https://newsapi.org/v2/top-headlines?country={country_code}&language=en&apiKey={apiKey}"
    else:
        return f"https://newsapi.org/v2/top-headlines?language=en&apiKey={apiKey}"
    


