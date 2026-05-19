import numpy as np
import pandas as pd
from scipy import stats

# 1. MEMBUAT SIMULASI DATA EKSPERIMEN (A/B TESTING) - SPLITWISE SMART BUDGETING
# Eksperimen difokuskan pada 1.000 pengguna kategori "Bad" (tabungan minus/kritis)
np.random.seed(42)  # Biar angka acaknya selalu konsisten tiap di-run
n_users = 500

# Grup A (Control): Pengguna kategori Bad TANPA fitur Smart Budgeting
# Rata-rata tabungan minus/defisit sekitar -Rp 500.000 karena gaya hidup berlebih
savings_control = np.random.normal(loc=-500000, scale=300000, size=n_users)

# Grup B (Treatment): Pengguna kategori Bad DENGAN fitur Smart Budgeting
# Rata-rata tabungan membaik menjadi positif sekitar Rp 450.000 (bergeser ke Average)
savings_treatment = np.random.normal(loc=450000, scale=250000, size=n_users)

# Gabungkan ke dalam satu DataFrame Pandas
df_ab = pd.DataFrame({
    'User_ID': range(1, (n_users * 2) + 1),
    'Group': ['Control (Tanpa Smart Budgeting)'] * n_users + ['Treatment (Pakai Smart Budgeting)'] * n_users,
    'Savings': np.concatenate([savings_control, savings_treatment])
})

print("=== RINGKASAN DATA EKSPERIMEN (FOKUS KATEGORI BAD) ===")
summary = df_ab.groupby('Group')['Savings'].agg(['count', 'mean', 'std']).round(2)
summary.columns = ['Jumlah Pengguna', 'Rata-rata Tabungan (Rp)', 'Standar Deviasi']
print(summary)
print("\n" + "="*75 + "\n")


# 2. UJI STATISTIK MENGGUNAKAN TWO-SAMPLE T-TEST
# Hipotesis kita:
# H0 (Null Hypothesis): Fitur Smart Budgeting GAK NGARUH (Tabungan B sama-sama minus seperti A).
# H1 (Alternative Hypothesis): Fitur Smart Budgeting NGARUH (Tabungan B meningkat signifikan jadi positif).

t_stat, p_value = stats.ttest_ind(savings_treatment, savings_control, equal_var=False)

print("=== HASIL UJI T-TEST STATISTIK ===")
print(f"T-Statistic : {t_stat:.4f}")
print(f"P-Value     : {p_value:.6f}")


# 3. KESIMPULAN OTOMATIS BERSYARAT
alpha = 0.05  # Batas toleransi error standar (5%)

if p_value < alpha:
    print("\n KESIMPULAN: EKSPERIMEN BERHASIL (SIGNIFIKAN)!")
    print(f"Karena P-Value ({p_value:.6f}) < 0.05, kita MENOLAK H0.")
    print("Artinya, implementasi fitur 'Smart Budgeting' secara nyata berhasil")
    print("mengontrol pengeluaran gaya hidup dan menyelamatkan pengguna dari defisit,")
    print("sehingga menggeser status mereka dari 'Bad' menjadi 'Average'.")
else:
    print("\n KESIMPULAN: EKSPERIMEN GAGAL (TIDAK SIGNIFIKAN)!")
    print(f"Karena P-Value ({p_value:.6f}) >= 0.05, kita GAGAL MENOLAK H0.")
    print("Artinya, fitur baru belum cukup kuat untuk menekan pengeluaran gaya hidup pengguna.")