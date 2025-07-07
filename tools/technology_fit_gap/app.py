
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Technology Fit-Gap Matrix", layout="wide")
st.title("Technology Fit-Gap Matrix")

file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "sample_data", "tech_fit_gap.csv"))
if os.path.exists(file):
    df = pd.read_csv(file)
    st.dataframe(df)
    st.bar_chart(df["Fit"].value_counts())
else:
    st.warning("No fit-gap data found.")
