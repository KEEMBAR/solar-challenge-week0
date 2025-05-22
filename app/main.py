import streamlit as st
from app.utils import load_data, boxplot_metric, top_regions_by_metric

st.set_page_config(page_title="Solar Potential Dashboard", layout="wide")
st.title("🌞 Solar Potential Explorer")

# Load Data
df = load_data()

# Sidebar Controls
country_options = df["Country"].unique().tolist()
selected_metric = st.selectbox("Select Metric", ["GHI", "DNI", "DHI"])

# Filtered Data
filtered_df = df[df["Country"].isin(country_options)]

# Main Section
st.subheader(f"Boxplot of {selected_metric}")
fig = boxplot_metric(filtered_df, selected_metric)
st.pyplot(fig)

# Top regions summary (optional)
st.subheader(f"Top Countries by Average {selected_metric}")
st.write(top_regions_by_metric(filtered_df, selected_metric))
