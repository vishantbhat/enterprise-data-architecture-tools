
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Tech Landscape", layout="wide")
st.title("Technology Landscape Matrix")

file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "sample_data", "tech_landscape.csv"))
if os.path.exists(file):
    df = pd.read_csv(file)
    st.dataframe(df)
    st.bar_chart(df["Layer"].value_counts())
else:
    st.warning("No tech data found.")
