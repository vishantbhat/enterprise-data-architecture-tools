
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Transformation Principles", layout="wide")
st.title("Transformation Principles Register")

file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "sample_data", "principles.csv"))
if os.path.exists(file):
    df = pd.read_csv(file)
    st.dataframe(df)
    st.bar_chart(df["Category"].value_counts())
else:
    st.warning("Principles file not found.")
