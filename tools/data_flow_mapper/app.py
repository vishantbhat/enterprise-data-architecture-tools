import streamlit as st
import pandas as pd
import graphviz

st.set_page_config(page_title="Data Flow Mapper", layout="wide")
st.title("🔁 Data Flow Mapper")

# Initialize session state
if "flows" not in st.session_state:
    st.session_state.flows = []

# Sidebar form to add a new data flow
st.sidebar.header("➕ Add Data Flow")
with st.sidebar.form("flow_form"):
    source = st.text_input("Source System")
    target = st.text_input("Target System")
    interface = st.text_input("Interface Name / Protocol")
    frequency = st.selectbox("Frequency", ["Real-Time", "Hourly", "Daily", "Weekly", "Ad Hoc"])
    notes = st.text_area("Notes / Description")
    submitted = st.form_submit_button("Add Flow")

    if submitted and source and target:
        st.session_state.flows.append({
            "Source": source,
            "Target": target,
            "Interface": interface,
            "Frequency": frequency,
            "Notes": notes
        })
        st.success(f"Flow added: {source} → {target}")

# Display current flows
st.subheader("📋 Current Data Flows")
if st.session_state.flows:
    df = pd.DataFrame(st.session_state.flows)
    st.dataframe(df, use_container_width=True)

    # Export CSV
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download Flows as CSV", data=csv, file_name="data_flows.csv", mime="text/csv")

    # Render Graph
    st.subheader("📈 Visual Flow Diagram")
    dot = graphviz.Digraph()

    for flow in st.session_state.flows:
        label = f"{flow['Interface']}\n({flow['Frequency']})"
        dot.edge(flow["Source"], flow["Target"], label=label)

    st.graphviz_chart(dot)

else:
    st.info("No data flows yet. Use the sidebar to add flows.")
