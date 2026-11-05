#Konversi Waktu#

nilai = input("detik : ")
satuan = 60
detik = int(nilai)

hari = int(detik / (satuan * satuan * 24))
detik = int(detik - (satuan * satuan * 24) * hari)

jam = int(detik / (satuan * satuan))
detik = 