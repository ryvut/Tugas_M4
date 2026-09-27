nilai_pelter = [75, 80, 60, 95, 80, 85, 65, 100, 80]

jumlah_80 = nilai_pelter.count(80)
print("Jumlah mahasiswa yang mendapat nilai 80:", jumlah_80)

nilai_pelter.sort(reverse=True)
print("Nilai terurut (Tertinggi ke Terendah):", nilai_pelter)

top_3 = nilai_pelter[:3]
print("3 nilai tertinggi untuk penghargaan:", top_3)