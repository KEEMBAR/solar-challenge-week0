import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def load_data():
    df_benin = pd.read_csv('data/clean/benin_clean.csv')
    df_benin['Country'] = 'Benin'

    df_togo = pd.read_csv('data/clean/togo_clean.csv')
    df_togo['Country'] = 'Togo'

    df_sierra = pd.read_csv('data/clean/sierra_leone_clean.csv')
    df_sierra['Country'] = 'Sierra Leone'

    df_all = pd.concat([df_benin, df_togo, df_sierra], ignore_index=True)
    return df_all

def plot_boxplot(df, metric, countries):
    filtered_df = df[df['Country'].isin(countries)]
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(x='Country', y=metric, data=filtered_df, palette='Set2', ax=ax)
    ax.set_title(f'{metric} Distribution by Country')
    ax.set_xlabel('Country')
    ax.set_ylabel(metric)
    st.pyplot(fig)

def get_summary_stats(df, metric):
    summary = df.groupby('Country')[metric].agg(['mean', 'median', 'std']).reset_index()
    summary.columns = ['Country', 'Mean', 'Median', 'Std Dev']
    return summary

def get_top_regions(df, metric='GHI', top_n=5):
    return df.groupby(['Country', 'Region'])[metric].mean().reset_index().sort_values(by=metric, ascending=False).head(top_n)
