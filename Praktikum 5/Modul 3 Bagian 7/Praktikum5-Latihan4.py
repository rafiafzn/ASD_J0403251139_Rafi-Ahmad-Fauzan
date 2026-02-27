#------------------------------------------------------------------------------
# Nama: Rafi Ahmad Fauzan
# NIM: J0403251139
# Kelas: A|P2
#------------------------------------------------------------------------------

# ========================================================== 
# Latihan 4: Kombinasi Huruf 
# ========================================================== 
 
# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================

def kombinasi(n, hasil=""):

    # jika panjang hasil sudah sama dengan n
    # berarti kombinasi sudah lengkap
    if len(hasil) == n:
        print(hasil)
        return

    # tambahkan huruf A lalu lanjut rekursi
    kombinasi(n, hasil + "A")

    # tambahkan huruf B lalu lanjut rekursi
    kombinasi(n, hasil + "B")


kombinasi(2)

# HASIL DISKUSI
# Total kombinasi = 2^n karena tiap posisi bisa A atau B