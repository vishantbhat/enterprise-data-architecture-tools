
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="System Inventory Tracker", layout="wide")
st.title("System Inventory Tracker")

file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "sample_data", "inventory.csv"))
if os.path.exists(file):
    df = pd.read_csv(file)
    st.dataframe(df)
    st.bar_chart(df["Platform"].value_counts())
else:
    st.warning("Sample inventory data not found.")
