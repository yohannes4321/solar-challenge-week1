import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

@st.cache_data
def load_data():
    benin = pd.read_csv("data/benin_clean.csv")
    sl = pd.read_csv("data/sierra_leone_clean.csv")
    togo = pd.read_csv("data/togo_clean.csv")

    benin['Country'] = 'Benin'
    sl['Country'] = 'Sierra Leone'
    togo['Country'] = 'Togo'

    return pd.concat([benin, sl, togo], ignore_index=True)

def plot_boxplot(df, metric):
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x="Country", y=metric, palette="Set2", ax=ax)
    ax.set_title(f'{metric} by Country')
    ax.set_ylabel(f'{metric} (W/m²)')
    st.pyplot(fig)

def plot_avg_bar(df):
    avg_ghi = df.groupby("Country")["GHI"].mean().sort_values()
    fig, ax = plt.subplots()
    avg_ghi.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_ylabel('Average GHI (W/m²)')
    ax.set_title('Average GHI by Country')
    st.pyplot(fig)

def summary_table(df):
    return df.groupby('Country')[['GHI', 'DNI', 'DHI']].agg(['mean', 'median', 'std']).round(2)
