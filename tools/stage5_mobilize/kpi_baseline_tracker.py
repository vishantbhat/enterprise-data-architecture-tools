
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Kpi Baseline Tracker", layout="wide")
st.title("Kpi Baseline Tracker")

file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "sample_data", "kpi_baseline_tracker.csv"))
if os.path.exists(file):
    df = pd.read_csv(file)
    st.dataframe(df)
else:
    st.warning("Sample data not found.")
