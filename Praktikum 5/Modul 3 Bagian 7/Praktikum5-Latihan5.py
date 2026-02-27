#------------------------------------------------------------------------------
# Nama: Rafi Ahmad Fauzan
# NIM: J0403251139
# Kelas: A|P2
#------------------------------------------------------------------------------

# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================

def buat_pin(panjang, hasil=""):

    # jika panjang PIN sudah sesuai
    # langsung tampilkan hasilnya
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    # menambahkan angka satu per satu lalu rekursi
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)


buat_pin(3)

# HASIL DISKUSI
# Agar angka tidak berulang, bisa cek dulu apakah angka sudah ada atau simpen angka yang sudah dipakai lalu jangan dipakai lagi