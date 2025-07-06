import streamlit as st
import pandas as pd

st.set_page_config(page_title="Technical Debt Register", layout="wide")
st.title("💣 Technical Debt Register")

# Initialize session state
if "debts" not in st.session_state:
    st.session_state.debts = []

# Sidebar form to add technical debt
st.sidebar.header("➕ Add Technical Debt")
with st.sidebar.form("debt_form"):
    area = st.text_input("System / Area")
    issue = st.text_area("Issue Description")
    impact = st.selectbox("Impact", ["Low", "Medium", "High"])
    root_cause = st.text_input("Root Cause")
    proposed_solution = st.text_area("Proposed Solution")
    risk_rating = st.selectbox("Risk Rating", ["Low", "Medium", "High"])
    status = st.selectbox("Status", ["Identified", "Planned", "In Progress", "Resolved"])
    submitted = st.form_submit_button("Add Entry")

    if submitted and area and issue:
        st.session_state.debts.append({
            "System/Area": area,
            "Issue": issue,
            "Impact": impact,
            "Root Cause": root_cause,
            "Proposed Solution": proposed_solution,
            "Risk Rating": risk_rating,
            "Status": status
        })
        st.success(f"Issue logged under {area}")

# Display current register
st.subheader("📋 Technical Debt Log")
if st.session_state.debts:
    df = pd.DataFrame(st.session_state.debts)
    st.dataframe(df, use_container_width=True)

    # Export as CSV
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download Register as CSV", data=csv, file_name="technical_debt_register.csv", mime="text/csv")
else:
    st.info("No technical debt logged yet.")
