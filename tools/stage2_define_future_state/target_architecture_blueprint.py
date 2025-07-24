
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Target Architecture Blueprint", layout="wide")
st.title("Target Architecture Blueprint")

file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "sample_data", "target_architecture_blueprint.csv"))
if os.path.exists(file):
    df = pd.read_csv(file)
    st.dataframe(df)
else:
    st.warning("Sample data not found.")
