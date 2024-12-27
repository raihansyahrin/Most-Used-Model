# LLM Model Analytics - Tugas Akhir

Proyek ini merupakan bagian dari **Tugas Akhir** untuk mempelajari **Visualisasi Data** menggunakan **Streamlit**. Tujuan dari aplikasi ini adalah untuk memvisualisasikan dataset model bahasa yang paling banyak digunakan (LLMs), menunjukkan tren dan wawasan berdasarkan jumlah likes, penulis, dan penggunaan sepanjang waktu.

### Anggota Kelompok:

- Muhammad Faqih Abdussalam / 1301213056
- Muhamad Raihan Syahrin Sya’bani / 1301213257

## Hasil

Untuk hasilnya, silakan akses di [https://most-used-model.streamlit.app/](https://most-used-model.streamlit.app/)

## Fitur

Aplikasi ini terdiri dari beberapa halaman untuk menjelajahi berbagai aspek dari dataset:

- **Dashboard**: Ringkasan dataset dengan metrik kunci dan visualisasi.
- **Raw Data**: Menampilkan dataset mentah untuk pemeriksaan lebih mendalam.
- **Top Models by Likes**: Grafik yang mengurutkan model berdasarkan jumlah likes.
- **Filtered Visualization**: Menyaring dan memvisualisasikan data berdasarkan penulis, dengan pembaruan waktu nyata.

## Instalasi

Untuk menjalankan proyek ini secara lokal, ikuti langkah-langkah berikut:

1. Clone repository ini ke lokal Anda:

   ```bash
   git clone https://github.com/raihansyahrin/Most-Used-Model.git
   ```

2. Jalankan aplikasi Streamlit:
   ```bash
   streamlit run app.py
   ```

Aplikasi akan terbuka di browser Anda, di mana Anda dapat berinteraksi dengan data.

## Dataset

Dataset yang digunakan untuk proyek ini adalah `burtenshaw/most_used_models` dari pustaka `datasets` milik Hugging Face. Dataset ini berisi data tentang model-model LLM yang paling banyak digunakan, termasuk ID model, penulis, jumlah likes, dan tanggal modifikasi terakhir.

Dataset ini dimuat menggunakan kode berikut:

```python
from datasets import load_dataset

dataset = load_dataset("burtenshaw/most_used_models", split="train")
```
