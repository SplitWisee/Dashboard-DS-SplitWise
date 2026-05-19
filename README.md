#  SplitWise: Financial Analysis Dashboard

**SplitWise Dashboard** analisis keuangan interaktif yang dirancang untuk membantu Gen Z dan milenial memahami kesehatan finansial mereka. Dashboard ini mengolah lebih dari **31.000 data nasabah** untuk memberikan wawasan objektif mengenai kesiapan investasi dan perilaku pengeluaran.

---

##  Link Dashboard
Akses dashboard interaktif melalui tautan di bawah ini:  
 **[SplitWise Live Dashboard](https://dashboard-splitwise.streamlit.app/)**

---

## Deskripsi Proyek
Dashboard ini bukan sekadar alat visualisasi, melainkan solusi untuk masalah *financial awareness*. Dengan mengintegrasikan data dari berbagai sektor (*Marketing, Loan, & Credit*), SplitWise mampu memberikan:

- **Klasifikasi Otomatis:**  
  Menentukan status keuangan pengguna (**Good, Average, Bad**) berdasarkan rasio tabungan dan skor kredit.

- **Analisis Distribusi (Violin Plot):**  
  Menggunakan *Violin Plot* untuk melihat kepadatan distribusi pendapatan pengguna sehingga lebih informatif dibanding rata-rata biasa.

- **Deteksi Pengeluaran:**  
  Mengidentifikasi apakah beban finansial terbesar berasal dari gaya hidup atau kewajiban hutang (*credit card*).

- **Dynamic Insights:**  
  Penjelasan teks otomatis yang berubah sesuai dengan filter usia yang dipilih pengguna.

---

## 🧪 Eksperimen A/B Testing
Untuk mengatasi masalah utama di mana **Gaya Hidup** menjadi beban pengeluaran dominan, dilakukan eksperimen A/B Testing terhadap fitur baru: **Real-time Pop-up Budget Warning**.

- **Grup Control (A):** Pengguna tanpa fitur pengingat budget.
- **Grup Treatment (B):** Pengguna dengan fitur *real-time pop-up warning*.
- **Metrik Evaluasi:** Rata-rata tabungan (`savings`) bulanan pengguna.

## **Hasil Uji Statistik (Two-Sample T-Test):**
- **T-Statistic:** 7.0555
- **P-Value:** 0.000000 (Signifikan pada alpha = 5%)
**Kesimpulan Bisnis:** Karena $P-Value < 0.05$, $H_0$ ditolak. Implementasi fitur *Pop-up Warning* secara nyata dan signifikan terbukti berhasil mengontrol pengeluaran gaya hidup pengguna dan meningkatkan rata-rata tabungan bulanan mereka pada sistem SplitWise.
---

## Teknologi yang Digunakan

- Python
- streamlit
- pandas
- plotly
- numpy
- seaborn
- matplotlib
- scipy

---

## Langkah Instalasi (Lokal)

Jika ingin menjalankan project ini di perangkat lokal, ikuti langkah berikut:

### 1. Clone Repository
```bash
git clone https://github.com/SplitWisee/Dashboard-DS-SplitWise.git
cd Dashboard-DS-SplitWise
