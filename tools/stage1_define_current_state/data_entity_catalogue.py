
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Data Entity Catalogue", layout="wide")
st.title("Data Entity Catalogue")

file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "sample_data", "data_entity_catalogue.csv"))
if os.path.exists(file):
    df = pd.read_csv(file)
    st.dataframe(df)
else:
    st.warning("Sample data not found.")
