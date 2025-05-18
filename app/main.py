import streamlit as st
import pandas as pd
from app.utils import load_data, plot_boxplot, plot_avg_bar, summary_table

st.set_page_config(page_title="Solar Country Comparison", layout="wide")

st.title("Cross-Country Solar Radiation Dashboard")
st.markdown("Visualize and compare solar metrics across Benin, Sierra Leone, and Togo.")

# --- Data Loading ---
df_all = load_data()

# --- Metric Selection ---
metric = st.selectbox("Select Metric", ["GHI", "DNI", "DHI"])

# --- Boxplot ---
st.subheader(f"{metric} Distribution by Country")
plot_boxplot(df_all, metric)

# --- Summary Table ---
st.subheader("Summary Statistics")
st.dataframe(summary_table(df_all), use_container_width=True)

# --- Bar Chart ---
st.subheader("Average GHI by Country")
plot_avg_bar(df_all)

st.caption("Developed for MoonLight Energy Solutions - Solar Challenge")
