# Soal Seleksi Kandidat Pak Budi

data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

print("Data skor tes potensi akademik:", data)

# Jawaban Soal 1: Lima kandidat dengan nilai tertinggi, dari tinggi ke rendah
# Sort descending untuk mendapatkan tertinggi
data_desc = sorted(data, reverse=True)
lima_tertinggi = data_desc[:5]

print("\n1. Lima kandidat dengan nilai tertinggi (dari tinggi ke rendah):", lima_tertinggi)

# Jawaban Soal 2: Kandidat yang lolos (indeks)
lolos_indeks = []
for skor in lima_tertinggi:
    indeks = data.index(skor)
    lolos_indeks.append(indeks)

print("2. Kandidat yang lolos (indeks, diurutkan):", sorted(lolos_indeks))
