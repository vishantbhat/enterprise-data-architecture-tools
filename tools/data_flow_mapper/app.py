
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Data Flow Mapper", layout="wide")
st.title("Data Flow Mapper")

file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "sample_data", "data_flow.csv"))
if os.path.exists(file):
    df = pd.read_csv(file)
    st.dataframe(df)
    st.bar_chart(df["Flow Type"].value_counts())
else:
    st.warning("Data flow file not found.")
