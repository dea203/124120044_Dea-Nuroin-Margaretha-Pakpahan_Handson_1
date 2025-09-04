total = 0 
jumlah_anggota = int(input("jumlah anggota keluarga: "))
for i in range(1, jumlah_anggota + 1):
    usia = int(input(f"anggota keluarga ke-{i} :"))
    total = total + usia

rata_rata = total / jumlah_anggota
print("jumlah anggota keluarga:",jumlah_anggota)
print("total usia:", total)
print("rata rata usia keluarga:", rata_rata)