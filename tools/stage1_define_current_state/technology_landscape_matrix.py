
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Technology Landscape Matrix", layout="wide")
st.title("Technology Landscape Matrix")

file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "sample_data", "technology_landscape_matrix.csv"))
if os.path.exists(file):
    df = pd.read_csv(file)
    st.dataframe(df)
else:
    st.warning("Sample data not found.")
