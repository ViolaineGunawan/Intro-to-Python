#input nama nim nilai mhs 
mhs=input("Masukkan nama mahasiswa: ")
nim=input("Masukkan NIM: ")
nilai=int(input("Masukkan nilai ujian (0-100): "))

#output tipe data nama nim nilai mhs
print(f"Nama: {mhs} (type: < {type(mhs)} >)")
print(f"NIM: {nim} (type: <{type(nim)}>)")
print(f"Nilai: {nilai} (type: <{type(nilai)}>)\n")

#evaluasi nilai mhs sesuai gradenya lalu di cetak
print("Hasil Evaluasi:")
print(f"Mahasiswa: {mhs} (NIM: {nim})")
print(f"Nilai Ujian: {nilai}")
if nilai>84 and nilai<101:
  print("Kategori Nilai: A (Sangat Baik)")
elif nilai >74:
  print("Kategori Nilai: B (Baik)")
elif nilai >59:
  print("Kategori Nilai: C (Cukup)")
elif nilai >39:
  print("Kategori Nilai: D (Kurang)")
else:
  print("Kategori Nilai: E (Sangat Kurang)")