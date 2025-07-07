
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Migration Plan", layout="wide")
st.title("High-Level Migration Plan")

file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "sample_data", "migration_plan.csv"))
if os.path.exists(file):
    df = pd.read_csv(file)
    st.dataframe(df)
    st.bar_chart(df["Timeline"].value_counts())
else:
    st.warning("Migration plan data not found.")
