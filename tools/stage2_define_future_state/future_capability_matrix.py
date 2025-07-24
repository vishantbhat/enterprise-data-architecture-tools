
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Future Capability Matrix", layout="wide")
st.title("Future Capability Matrix")

file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "sample_data", "future_capability_matrix.csv"))
if os.path.exists(file):
    df = pd.read_csv(file)
    st.dataframe(df)
else:
    st.warning("Sample data not found.")
