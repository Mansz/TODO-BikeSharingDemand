# Proyek Analisis Data: Bike Sharing Demand

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data penyewaan sepeda untuk memahami faktor-faktor yang mempengaruhi penggunaan sepeda dan tren penggunaannya dari waktu ke waktu.

## Setup Environment

### Setup Environment - Anaconda
Jika Anda menggunakan Anaconda, ikuti langkah-langkah berikut:

1. Buat lingkungan baru:
   ```bash
   conda create --name main-ds python=3.9
2.  Aktivkan lingkungan :
   conda activate main-ds
3. Instal dependensi:
   pip install -r requirements.txt

### Setup Environment - Shell/Terminal
Jika Anda menggunakan shell atau terminal, ikuti langkah-langkah berikut:
1. Buat direktori untuk proyek
mkdir proyek_analisis_data
cd proyek_analisis_data
2. Instal pipenv:
pip install pipenv
3. Buat lingkungan virtual dan aktifkan:
pipenv install
pipenv shell
4. Instal dependensi
pip install -r requirements.txt


### Run Dashboard
streamlit run dashboard/dashboard.py

