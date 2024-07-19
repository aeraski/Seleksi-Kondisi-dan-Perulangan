def nilai_akhir(tugas, uts, uas):
    nilai = (tugas * 0.2)+(uts * 0.3)+(uas * 0.5)
    if nilai >= 60:
        return "Lulus"
    else:
        return "Tidak Lulus"
    
tugas = float(input("Masukkan Nilai tugas: "))
uts = float(input("Masukkan Nilai uts: "))
uas = float(input("Masukkan Nilai uas: "))

hasil = nilai_akhir(tugas, uts, uas)
print(hasil)

