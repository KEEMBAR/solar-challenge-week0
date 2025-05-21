# utils.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath):
    """Load CSV data into a DataFrame."""
    return pd.read_csv(filepath)

def impute_missing_values(df, column, method='mean'):
    """Impute missing values in a column."""
    if method == 'mean':
        df[column].fillna(df[column].mean(), inplace=True)
    elif method == 'median':
        df[column].fillna(df[column].median(), inplace=True)
    return df

def plot_histogram(df, column, bins=20, color='blue'):
    """Plot a histogram for a given column."""
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column].dropna(), bins=bins, color=color, kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def summarize_missing(df):
    """Print summary of missing values per column."""
    missing = df.isnull().sum()
    print("Missing values per column:")
    print(missing[missing > 0])
