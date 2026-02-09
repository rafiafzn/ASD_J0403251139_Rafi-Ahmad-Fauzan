#=========================================================
# Praktikum 2 - Konsep ADT dan File Handling (STUID KASUS)
# Latihan 1: Membuat File dan 
#=========================================================

# variabel menyimpan data file
nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {}  # inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            if not baris:
                continue
            parts = [p.strip() for p in baris.split(',')]
            if len(parts) != 3:
                continue
            nim, nama, nilai = parts
            try:
                nilai_int = int(nilai)
            except ValueError:
                continue
            data_dict[nim] = {"nama": nama, "nilai": nilai_int}
    return data_dict


buka_data = baca_data(nama_file)
print('jumlah yang terbaca', len(buka_data))


#=========================================================================================
# Praktikum 2: Konsep ADT dan File Handling
#Latihan 2: Membuat fungsi menampilkan data
#===========================================================================================

def tampilkan_data(data_dict):
    # membuat header tabel
    print("\n======= DAFTAR MAHASISWA =======")
    print(f"{'NIM': <10}| {'Nama': <12} | {'Nilai': >5}")
    print("-"*33)  # membuat garis

    # menampilkan isi datanya
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {int(nilai):>5}")


tampilkan_data(buka_data)


# =====================================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 3: Membuat Fungsi Mencari Data
# =====================================================================

#membuat fungsi pencarian data
def cari_data(data_dict):
    #pencarian data berdasarkan nim sebagai key dictionary
    #membuat input nim mahasiswa yang akan dicari
    nim_cari = input("Masukkan NIM mahasiswa yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("===== Data Mahasiswa Ditemukan =====")
        print(f"NIM   : {nim_cari}")
        print(f"Nama  : {nama}")
        print(f"Nilai : {nilai}")
    else:
        print("Data tidak ditemukan. Pastikan NIM yang dimasukkan benar")

#memanggil fungsi cari data
cari_data(buka_data)

def ubah_data(data_dict):
    #awali dulu dengan mencari NIM / Data Mahasiswa yang ingin di ubah
    nim = input("Masukkan NIM yang akan diubah :").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan. Pastikan NIM yang dimasukkan benar")
        return

    try:
        nilai_baru = int(input("Masukkan nilai baru 0-100 :").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update Dibatalkan")

    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0-100. Update Dibatalkan")

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update Berhasil. Nilai {nim} dari {nilai_lama} menjadi {nilai_baru}")

#memanggil fungsi
ubah_data(buka_data)

# ===============================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan   5: Membuat Fungsi Simpan Data
# ===============================================

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")


#memanggil fungsi
simpan_data(nama_file, buka_data)
print("\nData Berhasil Disimpan ke file: ", nama_file)


def main():
    buka_data = baca_data(nama_file)
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Update Data Mahasiswa")
        print("4. Simpan Data ke File")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
             ubah_data(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
            print("Data berhasil disimpan ke file:", nama_file)
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == '__main__':
    main()

