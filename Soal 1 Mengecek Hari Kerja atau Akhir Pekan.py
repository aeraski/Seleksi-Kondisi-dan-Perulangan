def cek_hari_kerja(hari):
    # Mengubah input menjadi lowercase
    hari = hari.lower()

    # Menentukan hari kerja atau akhir pekan dari sebuah input
    if hari == "senin" or hari == "selasa" or hari == "rabu" or hari == "kamis" or hari == "jumat":
        return "Hari Kerja"
    elif hari == "sabtu" or hari == "minggu":
        return "Akhir Pekan"
    else:
        return "Hari tidak valid"

# Meminta pengguna memasukkan hari
hari = input("Masukkan Hari: ")

# Memanggil fungsi dan mencetak hasil
hasil = cek_hari_kerja(hari)
print(hasil)