import streamlit as st
import requests

# Load API key from Streamlit secrets
api_key = st.secrets["coingecko"]["api_key"]

# CoinGecko API URL
url = "https://api.coingecko.com/api/v3/simple/price?ids=blockstack&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true&precision=full"

# Headers with API key
headers = {
    "accept": "application/json",
    "x-cg-pro-api-key": api_key
}

# Fetch the price data using your API key
response = requests.get(url, headers=headers)

# Parse the JSON response
data = response.json()
price = data["blockstack"]["usd"]

# Streamlit app configuration
st.set_page_config(page_title="Token Price", layout="wide")

# Display the price in the center of the screen
st.markdown(
    f"<h1 style='text-align: center; font-size: 80px;'>${price:.4f}</h1>",
    unsafe_allow_html=True
)

# Add some additional details if needed
st.markdown(
    f"<p style='text-align: center;'>Last updated price of Blockstack (STX) in USD.</p>",
    unsafe_allow_html=True
)
