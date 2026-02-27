#------------------------------------------------------------------------------
# Nama: Rafi Ahmad Fauzan
# NIM: J0403251139
# Kelas: A|P2
#------------------------------------------------------------------------------

# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================

def pangkat(a, n):
    # jika pangkat 0, hasilnya selalu 1
    if n == 0:
        return 1
    else:
        # fungsi memanggil dirinya sendiri dengan n dikurangi 1
        # setiap pemanggilan akan mengalikan nilai a
        return a * pangkat(a, n - 1)

# contoh pemanggilan fungsi
print(pangkat(2, 4))

# HASIL DISKUSI
# Base case: jika n = 0, hasil 1 supaya rekursi berhenti
# Recursive case: fungsi memanggil dirinya dengan n-1
#] Contoh 2^4 = 2 * 2 * 2 * 2 * 1 = 16


