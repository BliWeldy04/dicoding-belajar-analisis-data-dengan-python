import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import gdown

day_url = 'https://drive.google.com/uc?id=1vayydX55Pmc7p04MMDPsMfWdM9V_tJPF'
hour_url = 'https://drive.google.com/uc?id=1OkeX93izAoOUHiLBBgcFNiEae0VYzjO0'
day_path = 'day.csv'  
hour_path = 'hour.csv' 

gdown.download(day_url, day_path, quiet=False)
gdown.download(hour_url, hour_path, quiet=False)

day_df = pd.read_csv(day_path)
hour_df = pd.read_csv(hour_path)

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

hour_df['weekday'] = hour_df['dteday'].dt.dayofweek  

st.title("Dashboard Bike Sharing")

st.header("Visualisasi")

temp_range = st.slider("Pilih Rentang Temperatur", min_value=0.0, max_value=1.0, value=(0.0, 1.0))
filtered_day_df = day_df[(day_df['temp'] >= temp_range[0]) & (day_df['temp'] <= temp_range[1])]

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='weathersit', y='cnt', data=filtered_day_df, ax=ax, palette="Blues_d")
ax.set_title('Pengaruh Kondisi Cuaca terhadap Jumlah Penyewaan Sepeda', fontsize=16)
ax.set_xlabel('Kondisi Cuaca', fontsize=12)
ax.set_ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
ax.set_xticklabels(['Cerah', 'Berawan', 'Ringan Hujan/Salju', 'Hujan Lebat/Salju'])
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='weekday', y='cnt', data=day_df, ax=ax, palette="Spectral")
ax.set_title('Pola Penyewaan Sepeda Berdasarkan Hari dalam Seminggu', fontsize=16)
ax.set_xlabel('Hari dalam Seminggu', fontsize=12)
ax.set_ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
ax.set_xticklabels(['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'])
st.pyplot(fig)

day_options = ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu']
selected_day = st.selectbox("Pilih Hari", options=day_options)

day_mapping = {'Minggu': 6, 'Senin': 0, 'Selasa': 1, 'Rabu': 2, 'Kamis': 3, 'Jumat': 4, 'Sabtu': 5}
selected_day_number = day_mapping[selected_day]

filtered_hour_df_by_day = hour_df[hour_df['weekday'] == selected_day_number]

if not filtered_hour_df_by_day.empty:
    average_hourly_rentals = filtered_hour_df_by_day.groupby('hr')['cnt'].mean().reset_index()

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='hr', y='cnt', data=average_hourly_rentals, ax=ax, palette="Oranges_d")
    ax.set_title(f'Rata-rata Penyewaan Sepeda Berdasarkan Jam dalam Sehari ({selected_day})', fontsize=16)
    ax.set_xlabel('Jam dalam Sehari', fontsize=12)
    ax.set_ylabel('Rata-rata Jumlah Penyewaan Sepeda', fontsize=12)
    st.pyplot(fig)