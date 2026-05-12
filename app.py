import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Konfigurasi Halaman
st.set_page_config(page_title="SplitWise Dashboard", layout="wide")

# 2. Fungsi Load Data (dengan perbaikan separator titik koma)
@st.cache_data
def load_data():
    # Menggunakan sep=';' karena file CSV kamu pakai titik koma
    data = pd.read_csv('databersihowi.csv', sep=';')
    # Bersihkan spasi di nama kolom
    data.columns = data.columns.str.strip()
    return data

# --- PENTING: Mendefinisikan variabel 'df' ---
df = load_data()

# 3. Sidebar untuk Filter
# --- BAGIAN ATAS SIDEBAR ---
with st.sidebar:
    st.image("splitwise.png", width=150) # Kamu bisa atur lebarnya di sini
    st.header("SPLITWISE")
    st.header("Filter Dashboard")
    

# 1. Slider Usia (Tetap sama)
age_filter = st.sidebar.slider("Pilih Rentang Usia", 
                               int(df['age'].min()), 
                               int(df['age'].max()), 
                               (20, 50))

st.sidebar.divider()

# 2. Checkbox untuk Status Budget dengan Deskripsi
st.sidebar.subheader("Pilih Status Budget:")
st.sidebar.caption("Filter kondisi keuangan pengguna:")

# Kita buat checkbox satu per satu agar bisa dikasih deskripsi
col_good = st.sidebar.checkbox("✅ Good (Sehat & Siap Investasi)", value=True)
col_avg  = st.sidebar.checkbox("🔵 Average (Stabil tapi Perlu Waspada)", value=True)
col_bad  = st.sidebar.checkbox("❌ Bad (Risiko Tinggi/Tabungan Minus)", value=True)

# Masukkan pilihan ke dalam list untuk memfilter dataframe
selected_status = []
if col_good: selected_status.append("Good")
if col_avg:  selected_status.append("Average")
if col_bad:  selected_status.append("Bad")

# Filter data berdasarkan input
df_filtered = df[(df['age'] >= age_filter[0]) & 
                 (df['age'] <= age_filter[1]) & 
                 (df['budget_status'].isin(selected_status))]

# 4. Header & Ringkasan Utama (Metrics)

st.title("💰 SplitWise - Financial Analysis Dashboard")
st.markdown("Dashboard ini menganalisis kesiapan investasi dan kesehatan finansial pengguna.")

col1, col2, col3 = st.columns(3)
col1.metric("Total Pengguna", f"{len(df_filtered):,}")
col2.metric("Rata-rata Skor Kredit", f"{int(df_filtered['credit_score'].mean())}")
col3.metric("Rata-rata Tabungan", f"Rp {df_filtered['savings'].mean():,.0f}")

st.divider()

# 5. Visualisasi Baris Pertama
left_col, right_col = st.columns(2)

with left_col:
    st.subheader("📊 Proporsi Kesiapan Investasi")
    fig_pie = px.pie(df_filtered, names='budget_status', 
                     color='budget_status',
                     color_discrete_map={'Good':'#2ecc71', 'Average':'#3498db', 'Bad':'#e74c3c'},
                     hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)

with right_col:
    st.subheader("📈 Distribusi Pendapatan vs Status")
    fig_violin = px.violin(df_filtered, y="income", x="budget_status", 
                           color="budget_status", box=True, points="all",
                           color_discrete_map={'Good':'#2ecc71', 'Average':'#3498db', 'Bad':'#e74c3c'})
    st.plotly_chart(fig_violin, use_container_width=True)

# 6. Visualisasi Baris Kedua
st.subheader("💸 Perbandingan Beban Pengeluaran")
expense_data = pd.DataFrame({
    'Kategori': ['Gaya Hidup', 'Cicilan CC'],
    'Rata-rata Nilai': [df_filtered['lifestyle_expense'].mean(), df_filtered['cc_expense'].mean() * 12]
})
fig_bar = px.bar(expense_data, x='Kategori', y='Rata-rata Nilai', 
                 color='Kategori', color_discrete_sequence=['#4B0082', '#FF4500'])
st.plotly_chart(fig_bar, use_container_width=True)

# 7. Tabel Data
if st.checkbox("Tampilkan Mentah Data"):
    st.write(df_filtered.head(100))

# 8. Dynamic Insights
st.divider()
st.subheader("🧐 Analisis Cepat (Dynamic Insight)")

# Logika Pendapatan
avg_income = df_filtered['income'].mean()
if avg_income > df['income'].mean():
    income_msg = "lebih tinggi dari rata-rata keseluruhan pengguna."
else:
    income_msg = "cenderung lebih rendah, perlu waspada dalam alokasi dana."

# Logika Pengeluaran
avg_lifestyle = df_filtered['lifestyle_expense'].mean()
avg_cc = df_filtered['cc_expense'].mean() * 12
if avg_lifestyle > avg_cc:
    expense_msg = "Gaya Hidup (Lifestyle)"
else:
    expense_msg = "Cicilan Kartu Kredit (CC)"

# Menampilkan Penjelasan Otomatis
st.info(f"""
Berdasarkan filter usia **{age_filter[0]} - {age_filter[1]} tahun** yang kamu pilih:
1. **Profil Pendapatan:** Rata-rata pendapatan kelompok ini adalah **Rp {avg_income:,.0f}**, yang mana {income_msg}
2. **Beban Terbesar:** Pengeluaran yang paling menguras kantong di segmen ini adalah **{expense_msg}**.
3. **Kesiapan Investasi:** Terdapat **{len(df_filtered[df_filtered['budget_status'] == 'Good'])} orang** yang sudah siap investasi (Investment Ready) di jangkauan usia ini.
""")