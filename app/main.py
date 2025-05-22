# app/main.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from app.utils import load_data, get_summary_stats, plot_boxplot, get_top_regions

st.set_page_config(page_title="Solar Potential Dashboard", layout="wide")
st.title(" Solar Potential Dashboard")

# Sidebar options
st.sidebar.header("Filter Options")
countries = ["Benin", "Togo", "Sierra Leone"]
selected_countries = st.sidebar.multiselect("Select countries:", countries, default=countries)

# Load data
df_all = load_data()
df_filtered = df_all[df_all['Country'].isin(selected_countries)]

# Display summary statistics
st.header("Summary Statistics")
summary = get_summary_stats(df_filtered)
st.dataframe(summary)

# Boxplots
st.header("Solar Metrics by Country")
metric = st.selectbox("Select metric to visualize:", ["GHI", "DNI", "DHI"])
fig = plot_boxplot(df_filtered, metric)
st.pyplot(fig)

# Top regions
st.header("Top Regions by Average GHI")
top_regions = get_top_regions(df_filtered)
st.dataframe(top_regions)

st.markdown("---")
st.markdown("Developed for Week 0 Solar Challenge")