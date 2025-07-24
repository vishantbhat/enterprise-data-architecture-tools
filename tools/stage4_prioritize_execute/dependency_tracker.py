
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Dependency Tracker", layout="wide")
st.title("Dependency Tracker")

file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "sample_data", "dependency_tracker.csv"))
if os.path.exists(file):
    df = pd.read_csv(file)
    st.dataframe(df)
else:
    st.warning("Sample data not found.")
