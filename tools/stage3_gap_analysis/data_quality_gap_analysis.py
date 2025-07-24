
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Data Quality Gap Analysis", layout="wide")
st.title("Data Quality Gap Analysis")

file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "sample_data", "data_quality_gap_analysis.csv"))
if os.path.exists(file):
    df = pd.read_csv(file)
    st.dataframe(df)
else:
    st.warning("Sample data not found.")
