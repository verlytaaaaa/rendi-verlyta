
def pembatas():
    print ("-"*46)
def pembatas2():
    print ("-"*46)

dataDosen = []

# Menu
def menu():
    while True:
        pembatas()
        print (" Data List Dosen ".center(46,"="))
        pembatas()
        print ("1. Tambah Data")
        print ("2. Hapus Data")
        print ("3. Edit Data")
        print ("4. Daftar Dosen")
        print ("5. Cek Dosen")
        print ("6. Indeks Data")
        print ("7. Keluar")

        pembatas()
        pilihan = input("Pilih Menu:").upper
        if pilihan == "1" or pilihan == "TAMBAH DATA":
            tambahData()
        elif pilihan == "2" or pilihan == "HAPUS DATA":
            hapusData()
        elif pilihan == "3" or pilihan == "EDIT DATA":
            editData()
        elif pilihan == "4" or pilihan == "DAFTAR DOSEN":
            daftarDosen()
        elif pilihan == "5" or pilihan == "CEK DOSEN":
            cekData()
        elif pilihan == "6" or pilihan == "INDEKS DATA":
            indexData()
        elif pilihan == "7" or pilihan == "KELUAR PROGRAM":
            pembatas()
            print("KELUAR DARI PROGRAM" .center(46,"="))
            exit()



# Tambah Data
def tambahData():
    pembatas()
    print (" Penambahan Dosen ".center(46,"="))
    pembatas()
    while True:
        data = input("Masukkan Nama")
        dataDosen.append
        print(f'Data["{data}"] Berhasil Ditambahkan')
        pilihan = input("Tambahkan Barang Lagi (y/n): ")
        if pilihan =="y":
            pembatas()
            print (" Daftar Dosen ".center(46,"="))
            pembatas()
            print ("kode".center (18, ' '), "Nama Dosen".center (30, ' '), "\n")
            for i in dataDosen:
                print("|    ",(dataDosen.index(i)+1), "     |", (i).center(22,' '),"|")
            pembatas2()
        else:
            menu()

# Next
def next():
    lanjut= input("Tekan y Jika ingin Melanjutkan Program") and ("Tekan n Untuk Kembali ke Menu ").lower()
    if lanjut == "y":
        hapusData()
    elif lanjut == "n":
        menu()
    else:
        print("inputan Salah, Program Kembali ke Menu")
        menu()

def next2():
    lanjut= input("Tekan y Jika ingin Melanjutkan Program") and ("Tekan n Untuk Kembali ke Menu ").lower()
    if lanjut == "y":
        editData()
    elif lanjut == "n":
        menu()
    else:
        print("inputan Salah, Program Kembali ke Menu")
        menu()
#Hapus Data
def hapusData():
    pembatas()
    print (" Penghapusan Dosen ".center(46,"="))
    pembatas()
    while True:
        hapus=input("Masukkan Nana Dosen Yang Ingin Dihapus:")
        if hapus in dataDosen:
            dataDosen.remove(hapus)
            print(f'Barang ["{hapus}"] Berhasil Dihapus')
            next()
        else:
            print(f'Barang ["{hapus}"] Tidak Tersedia')
            next()

#Edit Data
def editData():
     pembatas()
     print (" Daftar Data ".center(46,"="))
     pembatas()
     for i in dataDosen:
        print("|    ",(dataDosen.index(i)+1), "     |", (i).center(22,' '),"|")
     while True:
        pembatas()
        print(" Perubahan Data ".center(46,"="))
        pembatas()
        cariData = str(input("Masukkan Nama Dosen Yang ingin diubah: "))
        if cariData in dataDosen:
            ubahke = input("Ubah Menjadi:")
            dataDosen[dataDosen.index(cariData)] = ubahke
            for i in dataDosen :
                print ("| Kode".center (18, ' '), (dataDosen.index (i)+1) ,"|", (i).center(22,' '), "|")
            pembatas()
            print(f'Data ["{cariData}"] Berhasil Diubah Menjadi ["{ubahke}"]')
            pembatas()
            next2()

# Daftar 
def daftarDosen():
     pembatas()
     print (" Daftar Data ".center(46,"="))
     pembatas()
     print ("kode".center (18, ' '), "Nama Dosen".center (30, ' '), "\n")
     for i in dataDosen:
         print("|    ",(dataDosen.index(i)+1), "     |", (i).center(22,' '),"|")
     pembatas2()
     exit=input("Tekan Enter Untuk Keluar")
     if exit == " ":
        menu()
     else:
        menu()

# PENGECEKAN
def cekData():
    pembatas()
    print (" Daftar Data ".center(46,"="))
    pembatas()
    cek=input("Masukkan Nama Dosen yang Ingin Dicari: ")
    if cek in dataDosen:
        print (f'Data ["{cek}"] Tersedia ')
    else:
        print (f'Data ["{cek}"] Tidak Tersedia ')

    lanjut= input("Tekan y Jika ingin Melanjutkan Program") and ("Tekan n Untuk Kembali ke Menu ").lower()
    if lanjut == "y":
        pass
    elif lanjut == "n":
        menu()
    else:
        print("inputan Salah, Program Kembali ke Menu")
        menu()


# Cek Index Dosen ---
def indexData():
    pembatas()
    print (" Daftar Data ".center(46,"="))
    pembatas()
    cek2=input("Cek Indeks Dosen:")
    if cek2 in dataDosen:
        print (f'Data ["{cek2}"] Terdapat Pada Indeks : {dataDosen.index(cek2)}')
    else:
        print (f'Data ["{cek2}"] Tidak Tersedia ')

    lanjut= input("Tekan y Jika ingin Melanjutkan Program") and ("Tekan n Untuk Kembali ke Menu ").lower()
    if lanjut == "y":
        pass
    elif lanjut == "n":
        menu()
    else:
        print("inputan Salah, Program Kembali ke Menu")
        menu()




menu()
            
