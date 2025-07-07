
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Capability Maturity Model", layout="wide")
st.title("Capability Maturity Model")

file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "sample_data", "capability_maturity.csv"))
if os.path.exists(file):
    df = pd.read_csv(file)
    st.dataframe(df)
    st.bar_chart(df.set_index("Domain")[["Current", "Target"]])
else:
    st.warning("No maturity data found.")
