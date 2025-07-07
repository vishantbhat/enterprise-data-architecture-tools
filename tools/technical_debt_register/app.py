
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Technical Debt Register", layout="wide")
st.title("Technical Debt Register")

file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "sample_data", "technical_debt.csv"))
if os.path.exists(file):
    df = pd.read_csv(file)
    st.dataframe(df)
    st.bar_chart(df["Severity"].value_counts())
else:
    st.warning("Technical debt file not found.")
