import numpy as np
import pandas as pd
from scipy import stats

# 1. MEMBUAT SIMULASI DATA EKSPERIMEN (A/B TESTING)
# Kita umpamakan eksperimen ini diuji ke 1.000 pengguna SplitWise (500 per grup)
np.random.seed(42)  # Biar angka acaknya selalu konsisten tiap di-run
n_users = 500

# Grup A (Control): Pengguna lama (Tanpa Pop-up Warning)
# Rata-rata tabungan bulanan diset sekitar Rp 1.500.000 dengan standar deviasi 300.000
savings_control = np.random.normal(loc=1500000, scale=300000, size=n_users)

# Grup B (Treatment): Pengguna baru (Pakai Pop-up Warning Gaya Hidup)
# Rata-rata tabungan bulanan diset naik ke Rp 1.620.000 karena mereka lebih ngerem belanja
savings_treatment = np.random.normal(loc=1620000, scale=280000, size=n_users)

# Gabungkan ke dalam satu DataFrame Pandas
df_ab = pd.DataFrame({
    'User_ID': range(1, (n_users * 2) + 1),
    'Group': ['Control'] * n_users + ['Treatment'] * n_users,
    'Savings': np.concatenate([savings_control, savings_treatment])
})

print("=== 📊 RINGKASAN DATA EKSPERIMEN ===")
summary = df_ab.groupby('Group')['Savings'].agg(['count', 'mean', 'std']).round(2)
summary.columns = ['Jumlah Pengguna', 'Rata-rata Tabungan (Rp)', 'Standar Deviasi']
print(summary)
print("\n" + "="*50 + "\n")


# 2. UJI STATISTIK MENGGUNAKAN TWO-SAMPLE T-TEST (INDEPENDENT T-TEST)
# Hipotesis kita:
# H0 (Null Hypothesis): Fitur baru GAK NGARUH (Rata-rata tabungan A sama dengan B).
# H1 (Alternative Hypothesis): Fitur baru NGARUH (Rata-rata tabungan B lebih besar/berbeda signifikan dari A).

t_stat, p_value = stats.ttest_ind(savings_treatment, savings_control, equal_var=False)

print("=== 🧪 HASIL UJI T-TEST STATISTIK ===")
print(f"T-Statistic : {t_stat:.4f}")
print(f"P-Value     : {p_value:.6f}")


# 3. KESIMPULAN OTOMATIS BERSYARAT
alpha = 0.05  # Batas toleransi error standar (5%)

if p_value < alpha:
    print("\n🟢 KESIMPULAN: EKSPERIMEN BERHASIL (SIGNIFIKAN)!")
    print(f"Karena P-Value ({p_value:.6f}) < 0.05, kita MENOLAK H0.")
    print("Artinya, implementasi fitur 'Pop-up Warning' secara nyata dan signifikan")
    print("berhasil meningkatkan rata-rata tabungan bulanan pengguna SplitWise.")
else:
    print("\n🔴 KESIMPULAN: EKSPERIMEN GAGAL (TIDAK SIGNIFIKAN)!")
    print(f"Karena P-Value ({p_value:.6f}) >= 0.05, kita GAGAL MENOLAK H0.")
    print("Artinya, peningkatan tabungan yang terjadi hanya faktor kebetulan semata,")
    print("dan fitur baru belum memberikan dampak perubahan yang berarti.")