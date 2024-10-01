import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
day_data = pd.read_csv('../data/day.csv')
hour_data = pd.read_csv('../data/hour.csv')

# Title of the dashboard
st.title('Dashboard Penyewaan Sepeda')

# Display the day data
st.subheader('Data Harian')
st.write(day_data)

# Display the hour data
st.subheader('Data Jam')
st.write(hour_data)

# Visualisasi: Distribusi Jumlah Penyewaan dari Data Harian
st.subheader('Distribusi Jumlah Penyewaan (Data Harian)')
fig, ax = plt.subplots()
sns.histplot(day_data['cnt'], bins=30, kde=True, ax=ax)
ax.set_title('Distribusi Jumlah Penyewaan')
ax.set_xlabel('Jumlah Penyewaan')
ax.set_ylabel('Frekuensi')
st.pyplot(fig)

# Visualisasi: Distribusi Jumlah Penyewaan dari Data Jam
st.subheader('Distribusi Jumlah Penyewaan (Data Jam)')
fig_hour, ax_hour = plt.subplots()
sns.histplot(hour_data['cnt'], bins=30, kde=True, ax=ax_hour)
ax_hour.set_title('Distribusi Jumlah Penyewaan per Jam')
ax_hour.set_xlabel('Jumlah Penyewaan')
ax_hour.set_ylabel('Frekuensi')
st.pyplot(fig_hour)