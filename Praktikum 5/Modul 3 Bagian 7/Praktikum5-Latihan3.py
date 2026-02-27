#------------------------------------------------------------------------------
# Nama: Rafi Ahmad Fauzan
# NIM: J0403251139
# Kelas: A|P2
#------------------------------------------------------------------------------

# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================

def cari_maks(data, index=0):

    # jika sudah sampai elemen terakhir
    # langsung kembalikan nilainya
    if index == len(data) - 1:
        return data[index]

    # memanggil fungsi untuk mengecek sisa data
    maks_sisa = cari_maks(data, index + 1)

    # membandingkan nilai sekarang dengan hasil dari sisa data
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa


angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))

# HASIL DISKUSI
# Base case: jika sudah di elemen terakhir, langsung kembalikan nilainya
# Recursive case: fungsi memanggil dirinya untuk cek sisa data (index+1)
# Lalu nilai sekarang dibandingkan dengan hasil dari sisa data
# Alur: program mencari nilai terbesar satu per satu sampai akhir