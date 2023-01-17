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
print("= 1. Daftar Dosen                  =")
print("= 2. Tambah Dosen                  =")
print("= 3. Hapus Dosen                   =")
print("= 4. Cari Dosen                    =")
print("= 5. Keluar                        =")
print("====================================")

while(loop):
 print("\n\n")
 menu = int(input("Masukan menu : "))

 if menu == 1:
  for i in DaftarDosen:
   i = open("data.txt")
   for x in i:
    print(x)
    i.close()
   print("Nama :", DaftarDosen[i].getNama())
   print("Nim :", DaftarDosen[i].getNim())
   

 elif menu == 2:
  nama = str(input("Masukan nama : "))
  Nip = str(input("Masukan nip : "))
  dosen = dosen(nama, nim)
  DaftarDosen[nim] = dosen

 elif menu == 3:
  Nip = str(input("Masukan nip : "))
  if(nip in DaftarDosen):
   del DaftarDosen[nip]
  else:
   print("Data tidak ditemukan!!!")

 elif menu == 4:
  nip = str(input("Masukan nip : "))
  if(nip in DaftarDosen):
   print("Nama : ", DaftarDosen[nip].getNama())
   print("Nip : ", DaftarDosen[nip].getNim())
  else:
   print("Data tidak ditemukan!!!")

