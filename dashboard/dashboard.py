import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load datasets
day_data = pd.read_csv('../data/day.csv')
hour_data = pd.read_csv('../data/hour.csv')

# Title of the dashboard
st.title('Dashboard Penyewaan Sepeda')

# Display the first few rows of the datasets
st.subheader('Data Harian')
st.write(day_data.head())

# Pertanyaan 1: Pengaruh cuaca terhadap jumlah penyewaan sepeda
st.subheader('Distribusi Jumlah Penyewaan Berdasarkan Cuaca')
plt.figure(figsize=(10, 6))
sns.boxplot(x='weathersit', y='cnt', data=day_data)
plt.title('Count Distribution by Weather Situation')
plt.xlabel('Weather Situation')
plt.ylabel('Count of Rentals')
plt.xticks([0, 1, 2, 3], ['Clear', 'Mist', 'Light Rain', 'Heavy Rain'])
st.pyplot(plt)

# Pertanyaan 2: Tren penggunaan sepeda dari waktu ke waktu
st.subheader('Tren Penyewaan Sepeda Seiring Waktu')
hour_data['dteday'] = pd.to_datetime(hour_data['dteday'])
trend_data = hour_data.groupby('dteday').sum().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x='dteday', y='cnt', data=trend_data)
plt.title('Total Bike Rentals Over Time')
plt.xlabel('Date')
plt.ylabel('Total Count of Rentals')
plt.xticks(rotation=45)
st.pyplot(plt)