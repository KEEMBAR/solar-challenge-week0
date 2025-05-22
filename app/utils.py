import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data():
    benin = pd.read_csv("data/clean/benin_clean.csv")
    togo = pd.read_csv("data/clean/togo_clean.csv")
    sierra = pd.read_csv("data/clean/sierra_leone_clean.csv")
    
    benin["Country"] = "Benin"
    togo["Country"] = "Togo"
    sierra["Country"] = "Sierra Leone"
    
    df_all = pd.concat([benin, togo, sierra], ignore_index=True)
    return df_all

def top_regions_by_metric(df, metric="GHI", top_n=5):
    return df.groupby("Country")[metric].mean().sort_values(ascending=False).head(top_n)

def boxplot_metric(df, metric="GHI"):
    sns.set(style="whitegrid")
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x="Country", y=metric, ax=ax)
    ax.set_title(f"{metric} by Country")
    return fig
