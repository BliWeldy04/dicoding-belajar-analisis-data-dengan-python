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

st.title("Dashboard Bike Sharing")

st.header("Visualisasi")

st.subheader("Pengaruh Cuaca terhadap Jumlah Penyewaan")
fig, ax = plt.subplots(figsize=(12, 6))  
sns.barplot(x='weathersit', y='cnt', data=day_df, ax=ax, palette="Blues_d")  
ax.set_title('Pengaruh Kondisi Cuaca terhadap Jumlah Penyewaan Sepeda', fontsize=16)  
ax.set_xlabel('Kondisi Cuaca', fontsize=12)  
ax.set_ylabel('Jumlah Penyewaan Sepeda', fontsize=12)  
ax.set_xticklabels(['Cerah', 'Berawan', 'Ringan Hujan/Salju', 'Hujan Lebat/Salju'])  
st.pyplot(fig)

plt.figure(figsize=(12, 6))
sns.scatterplot(x='temp', y='cnt', data=day_df, hue='hum', size='windspeed', palette="viridis", sizes=(20, 200))
plt.title('Pengaruh Temperatur dan Kelembapan terhadap Jumlah Penyewaan Sepeda', fontsize=16)
plt.xlabel('Temperatur (Ternormalisasi)', fontsize=12)
plt.ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
st.pyplot(plt)

st.subheader("Pola Penyewaan Berdasarkan Hari dan Jam")

fig, ax = plt.subplots(figsize=(12, 6)) 
sns.barplot(x='weekday', y='cnt', data=day_df, ax=ax, palette="Spectral")  
ax.set_title('Pola Penyewaan Sepeda Berdasarkan Hari dalam Seminggu', fontsize=16) 
ax.set_xlabel('Hari dalam Seminggu', fontsize=12)  
ax.set_ylabel('Jumlah Penyewaan Sepeda', fontsize=12) 
ax.set_xticklabels(['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'])  
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(12, 6)) 
sns.lineplot(x='hr', y='cnt', data=hour_df, ax=ax, color="orange")
ax.set_title('Pola Penyewaan Sepeda Berdasarkan Jam dalam Sehari', fontsize=16)  
ax.set_xlabel('Jam dalam Sehari', fontsize=12) 
ax.set_ylabel('Jumlah Penyewaan Sepeda', fontsize=12)  
st.pyplot(fig)