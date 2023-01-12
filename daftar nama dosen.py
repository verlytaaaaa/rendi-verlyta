def __init__(self, nm, no_induk):
  self.nama = str(nm)
  self.nim = str(no_induk)

 def getNama(self):
  return self.nama

 def getNip(self):
  return self.nip

 def setNama(self, nm):
  self.nama = nm

 def setNim(self, no_induk):
  self.nim = no_induk

DaftarDosen = {}
loop = True

print("====================================")
print("=         Daftar Data Dosen        =")
print("====================================")
print("= # MENU                           =")
print("= 1. Tambah Nama Dosen             =")
print("= 2. Hapus Nama Dosen              =")
print("= 3. Tampilkan Semua Dosen         =")
print("= 4. Cari Dosen                    =")
print("= 5. Tambah Nip Dosen              =")
print("= 6. Hapus Nip Dosen               =")
print("= 7. Tambah Matkul Dosen           =")
print("= 8. Hapus Matkul Dosen            =") 
print("= 0. Keluar                        =")
print("====================================")

while(loop):
 print("\n\n")
 menu = int(input("Masukan menu : "))

 if menu == 1:
  nama = str(input("Masukan nama : "))
  Nip = str(input("Masukan nip : "))
  dosen = dosen(nama, nim)
  DaftarDosen[nim] = dosen

 elif menu == 2:
  Nip = str(input("Masukan nip : "))
  if(nip in DaftarDosen):
   del DaftarDosen[nip]
  else:
   print("Data tidak ditemukan!!!")

 elif menu == 3:
  for i in DaftarDosen:
   print("Nama :", DaftarDosen[i].getNama())
   print("Nim :", DaftarDosen[i].getNim())

 elif menu == 4:
  nip = str(input("Masukan nip : "))
  if(nip in DaftarDosen):
   print("Nama : ", DaftarDosen[nip].getNama())
   print("Nip : ", DaftarDosen[nip].getNim())
  else:
   print("Data tidak ditemukan!!!")

 elif menu == 5:
  nip = str(input("Masukan nip : "))
  if(nip in DaftarDosen):
   namaBaru = str(input("Masukan Nama Baru : "))
   DaftarDosen[nip].setNama(namaBaru)
  else:
   print("Data tidak ditemukan!!!")

 elif menu == 6:
  nip = str(input("Masukan nip : "))
  if(nip in DaftarDosen):
   nipBaru = str(input("Masukan Nip Baru : "))
   DaftarDosen[nip].setNip(nipBaru)
   dosen = DaftarDosen[nip]
   DaftarDosen[nipBaru] = dosen
   del DaftarDosen[nip]
  else:
   print("Data tidak ditemukan!!!")

 elif menu == 7:
  print("Jumlah Dosen : ", len(DaftarDosen))
 elif menu == 0:
  loop = False
 else:

  print("XXXX")