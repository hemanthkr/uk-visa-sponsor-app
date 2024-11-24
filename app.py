from bs4 import BeautifulSoup as bs
import streamlit as st
import pandas as pd
import requests


st.title("UK Visa Sponsor List")

BASE_URL =  "https://www.gov.uk/government/publications/register-of-licensed-sponsors-workers"
ASSETS_URL = "https://assets.publishing.service.gov.uk/"

def get_download_url(base_url):
    response = requests.get(BASE_URL)
    soup = bs(response.content, 'html.parser')
    links = [link['href'] for link in soup.find_all('a')]
    for link in links:
        if link.startswith(ASSETS_URL):
            return link

data_url =  get_download_url(BASE_URL)

dataframe = pd.read_csv(data_url)

st.write(dataframe)
    
