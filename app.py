from pandas.core.generic import T
import streamlit as st
from main import get_simplified_list, get_secondary_list
import pandas as pd

st.set_page_config(layout="wide")
st.title("Commercial Real Estate Search")


website = st.selectbox("Select website", options=['commercialrealestate', 'realcommercial'])

with open("keywords.txt", "r") as f:
    keyword_options = [k.strip() for k in f.readlines() if k.strip()]

keywords = st.multiselect(
    "Keywords", options=keyword_options, default=keyword_options[:1])
# Allow user to add multiple new keywords
new_keywords = st.text_input("Add new keywords (comma separated, optional)")
if new_keywords.strip():
    new_keywords_list = [k.strip()
                        for k in new_keywords.split(",") if k.strip()]
    # Add new keywords to file if not present
    updated = False
    with open("keywords.txt", "a+") as f:
        for k in new_keywords_list:
            if k not in keyword_options:
                f.write(f"{k}\n")
                keyword_options.append(k)
                updated = True
    # No rerun, just update keyword_options and keywords in memory
    keywords = keywords + [k for k in new_keywords_list if k not in keywords]
page_no = st.number_input("Page Number", min_value=1, value=1)
page_size = st.number_input("Page Size", min_value=1, max_value=200, value=200)
sale_method = st.text_input(
    "Sale Method (comma separated, optional)", value="")

if sale_method.strip():
    sale_method_list = [int(x.strip())
                        for x in sale_method.split(",") if x.strip().isdigit()]
else:
    sale_method_list = []

if st.button("Get Listings"):
    with st.spinner("Fetching data...", show_time=True):
        try:
            if website=="commercialrealestate":
                df = get_simplified_list(
                    keywords=keywords,
                    page_no=page_no,
                    page_size=page_size,
                    sale_method=sale_method_list
                )
            elif website=="realcommercial":
                df = get_secondary_list(keywords=keywords)
            else:
                st.error("Please select a website")
            
            st.success(f"Found {len(df)} results.")
            if df is not None:
                # Make seoUrl column a clickable link
                df['seoUrl'] = df['seoUrl'].apply(
                    lambda x: f'<a href="{x}" target="_blank">Go to Listing</a>')
                st.write(df.to_html(escape=False, index=False),
                         unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error: {e}")

