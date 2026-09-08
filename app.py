import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Production Monitor", layout="wide")
st.title("AI-Powered Production Monitoring")
st.caption("Prototype dashboard for the Snapdragon AI Lab project")

try:
    df = pd.read_csv("../data/sample_production_data.csv")
    st.metric("Total Sample Events", int(df["sensor_events"].sum()))
    st.line_chart(df.set_index("timestamp")[["production_rate"]])
    st.dataframe(df, use_container_width=True)
except FileNotFoundError:
    st.warning("Sample data file not found.")
