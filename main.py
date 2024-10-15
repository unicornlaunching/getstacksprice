import streamlit as st
import requests

# Load API key from Streamlit secrets
api_key = st.secrets["coingecko"]["api_key"]

# CoinGecko API URL for Blockstack (STX)
url = "https://api.coingecko.com/api/v3/simple/price?ids=blockstack&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true&precision=full"

# Headers with API key
headers = {
    "accept": "application/json",
    "x-cg-pro-api-key": api_key
}

# Fetch the price data
response = requests.get(url, headers=headers)

# Check for successful response
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Print the response to see its structure in case of issues
    st.write(data)

    # Safely access the price information
    if "blockstack" in data:
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
    else:
        st.error("Token information for 'blockstack' not found in the API response.")
else:
    st.error(f"Failed to fetch data. Status code: {response.status_code}")
