from pandas.core.generic import T
import streamlit as st
from main import get_simplified_list
import pandas as pd

st.set_page_config(layout="wide")
st.title("Commercial Real Estate Search")

with open("keywords.txt", "r") as f:
    keyword_options = f.readlines()

keywords = st.multiselect(
    "Keywords", options=keyword_options, default=keyword_options[:1])
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
            results = get_simplified_list(
                keywords=keywords,
                page_no=page_no,
                page_size=page_size,
                sale_method=sale_method_list
            )
            st.success(f"Found {len(results)} results.")
            if results:
                df = pd.DataFrame(results)
                st.dataframe(df, hide_index=True)
        except Exception as e:
            st.error(f"Error: {e}")
