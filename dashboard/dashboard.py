import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- Dokumentasi ---
st.markdown("# Proyek Analisis Data: Penyewaan Sepeda")
st.markdown("- **Nama:** I Putu Hananda Weldy Nugraha")
st.markdown("- **Email:** weldynugraha@gmail.com")
st.markdown("- **ID Dicoding:** weldy_nugraha_4lJK")
st.markdown("## Pendahuluan")
st.markdown("Notebook ini berisi analisis data tentang penyewaan sepeda. Tujuan dari analisis ini adalah untuk memahami pengaruh cuaca dan pola penyewaan sepeda berdasarkan hari dalam seminggu atau jam dalam sehari.")
st.markdown("## Tahapan Analisis Data")
st.markdown("### 1. Import Library")
st.markdown("Pada tahap ini, kita akan mengimpor library yang dibutuhkan untuk analisis data, visualisasi, dan pemodelan. Library yang digunakan antara lain:")
st.markdown("- `pandas`: untuk manipulasi dan analisis data.")
st.markdown("- `numpy`: untuk komputasi numerik.")
st.markdown("- `matplotlib`: untuk membuat visualisasi statis.")
st.markdown("- `seaborn`: untuk membuat visualisasi statistik yang lebih menarik.")
st.markdown("- `sklearn`: untuk pemodelan machine learning (opsional).")
st.markdown("- `streamlit`: untuk membuat aplikasi web interaktif (opsional).")
st.code("""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import streamlit as st 
""")
st.markdown("### 2. Data Wrangling")
st.markdown("Tahap ini meliputi proses pengumpulan, penilaian, dan pembersihan data.")
st.markdown("#### 2.1 Gathering Data")
st.markdown("Data yang digunakan dalam analisis ini berasal dari dua file CSV yang di-hosting di Google Drive. Data tersebut berisi informasi tentang penyewaan sepeda harian (`day`) dan per jam (`hour`).")
st.code("""
url = 'https://drive.google.com/uc?id=1yL3ulHq_QTLRHifVjISmGCq9qKXaIHud'
day = pd.read_csv(url)

url2 = 'https://drive.google.com/uc?id=14vZd0xgkZgxEVqgLlQYWxhAxO9f3_ob3'
hour = pd.read_csv(url2)
""")
st.markdown("#### 2.2 Assessing Data")
st.markdown("Pada tahap ini, kita akan menilai kualitas data dengan melihat beberapa baris pertama data, informasi umum data, statistik deskriptif, dan memeriksa missing values.")
st.code("""
day.head()
hour.head()
day.info()
hour.info()
day.describe()
hour.describe()
day.isnull().sum()
hour.isnull().sum()
""")
st.markdown("#### 2.3 Cleaning Data")
st.markdown("Tahap ini meliputi proses pembersihan data, seperti mengisi missing values dan mengubah tipe data.")
st.code("""
day['temp'].fillna(day['temp'].mean(), inplace=True)
day['dteday'] = pd.to_datetime(day['dteday'])
""")
st.markdown("### 3. Exploratory Data Analysis (EDA)")
st.markdown("Pada tahap ini, kita akan melakukan eksplorasi data dengan membuat berbagai visualisasi untuk memahami hubungan antara variabel-variabel dalam dataset.")
st.code("""
# Visualisasi menggunakan seaborn
sns.barplot(x='weathersit', y='cnt', data=day)
plt.show()
""")
st.markdown("### 4. Visualization & Explanatory Analysis")
st.markdown("Tahap ini bertujuan untuk menjawab pertanyaan bisnis yang telah dirumuskan sebelumnya dengan visualisasi yang lebih informatif dan penjelasan yang detail.")
st.code("""
# Visualisasi dan penjelasan
plt.figure(figsize=(12, 6))
sns.barplot(x='weekday', y='cnt', data=day, palette="Spectral")
plt.title('Pola Penyewaan Sepeda Berdasarkan Hari dalam Seminggu', fontsize=16)
plt.show()
        
# Visualisasi ini menunjukkan bahwa jumlah penyewaan sepeda cenderung lebih tinggi pada hari kerja (Senin-Jumat) dibandingkan dengan akhir pekan (Sabtu-Minggu).
""")
st.markdown("### 5. Analisis Lanjutan (Opsional)")
st.markdown("Pada tahap ini, kita dapat melakukan analisis lanjutan seperti menghitung matriks korelasi antar variabel.")
st.code("""
correlation_matrix = day[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()
""")
st.markdown("### 6. Conclusion")
st.markdown("Tahap ini berisi kesimpulan dari hasil analisis dan saran berdasarkan insight yang didapatkan.")
st.markdown("""
# Kesimpulan

Berdasarkan hasil analisis, dapat disimpulkan bahwa:

- Kondisi cuaca memiliki pengaruh yang signifikan terhadap jumlah penyewaan sepeda.
- Terdapat pola penyewaan yang jelas berdasarkan hari dalam seminggu dan jam dalam sehari.

# Saran

- Berdasarkan hasil analisis, disarankan untuk memfokuskan strategi pemasaran pada saat cuaca cerah dan temperatur hangat.
- Perlu dipertimbangkan untuk menyediakan lebih banyak sepeda pada jam-jam sibuk dan hari kerja untuk memenuhi permintaan.
- Melakukan promosi khusus pada akhir pekan untuk meningkatkan jumlah penyewaan.
""")


# --- Load Data ---
url = 'https://drive.google.com/uc?id=1yL3ulHq_QTLRHifVjISmGCq9qKXaIHud'
day = pd.read_csv(url)
url2 = 'https://drive.google.com/uc?id=14vZd0xgkZgxEVqgLlQYWxhAxO9f3_ob3'
hour = pd.read_csv(url2)

# --- Visualisasi ---
st.subheader("Pengaruh Kondisi Cuaca")
plt.figure(figsize=(12, 6))
sns.barplot(x='weathersit', y='cnt', data=day, palette="Blues_d")
plt.title('Pengaruh Kondisi Cuaca terhadap Jumlah Penyewaan Sepeda', fontsize=16)
plt.xlabel('Kondisi Cuaca', fontsize=12)
plt.ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
plt.xticks(ticks=[0, 1, 2, 3], labels=['Cerah', 'Berawan', 'Ringan Hujan/Salju', 'Hujan Lebat/Salju'])
st.pyplot(plt)

st.subheader("Pola Penyewaan Berdasarkan Hari")
plt.figure(figsize=(12, 6))
sns.barplot(x='weekday', y='cnt', data=day, palette="Spectral")
plt.title('Pola Penyewaan Sepeda Berdasarkan Hari dalam Seminggu', fontsize=16)
plt.xlabel('Hari dalam Seminggu', fontsize=12)
plt.ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
plt.xticks(ticks=[0, 1, 2, 3, 4, 5, 6], labels=['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'])
st.pyplot(plt)

st.subheader("Pola Penyewaan Berdasarkan Jam")
plt.figure(figsize=(12, 6))
sns.lineplot(x='hr', y='cnt', data=hour, color="orange")
plt.title('Pola Penyewaan Sepeda Berdasarkan Jam dalam Sehari', fontsize=16)
plt.xlabel('Jam dalam Sehari', fontsize=12)
plt.ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
st.pyplot(plt)

st.subheader("Korelasi Antar Variabel")
correlation_matrix = day[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Korelasi Antar Variabel')
st.pyplot(plt)