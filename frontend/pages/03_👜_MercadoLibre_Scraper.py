import streamlit as st
import pandas as pd
import os
from services.web_scraper import run_scraper

st.title("WEB SCRAPPER  e_comerce - Mercado Libre")

search_query = st.text_input("Input an item to search on e_commerce - Mercado Libre:")

if search_query:
    st.write(f"Search results of item: {search_query}")

    df, file_name = run_scraper(search_query)

    if not df.empty:
        st.dataframe(df)

        with open(file_name, "rb") as f:
            st.download_button(
                label="⬇️ Download Excel",
                data=f,
                file_name="search_results.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        try:
            os.remove(file_name)
        except FileNotFoundError:
            pass
    else:
        st.error("No items found")
