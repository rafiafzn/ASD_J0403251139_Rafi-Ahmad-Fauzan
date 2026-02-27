#------------------------------------------------------------------------------
# Nama: Rafi Ahmad Fauzan
# NIM: J0403251139
# Kelas: A|P2
#------------------------------------------------------------------------------

# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================

def countdown(n):

    # jika sudah sampai 0, program berhenti
    if n == 0:
        print("Selesai")
        return

    # bagian sebelum memanggil fungsi lagi
    print("Masuk:", n)

    # fungsi memanggil dirinya dengan nilai n-1
    countdown(n - 1)

    # bagian setelah rekursi selesai
    print("Keluar:", n)


countdown(3)


# HASIL DISKUSI
# Base case: saat n == 0 program berhenti dan print "Selesai"
# Recursive call: countdown(n-1) dipanggil sampai n habis
# Print "Masuk" dijalankan saat turun rekursi
# Print "Keluar" dijalankan saat fungsi kembali naik