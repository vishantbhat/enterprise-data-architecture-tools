
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Capability Gap Matrix", layout="wide")
st.title("Capability Gap Matrix")

file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "sample_data", "capability_gap_matrix.csv"))
if os.path.exists(file):
    df = pd.read_csv(file)
    st.dataframe(df)
else:
    st.warning("Sample data not found.")
