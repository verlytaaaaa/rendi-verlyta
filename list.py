import csv
import os

csv_filename = 'contacts.csv'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("=== APLIKASI KONTAK ===")
    print("[1] Lihat Daftar Dosen")
    print("[2] Buat Baru")
    print("[3] Edit Nama Dosen")
    print("[4] Hapus Nama Dosen")
    print("[5] Cari Nama Dosen")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu> ")
    
    if(selected_menu == "1"):
        show_dosen()
    elif(selected_menu == "2"):
        create_dosen()
    elif(selected_menu == "3"):
        edit_dosen()
    elif(selected_menu == "4"):
        delete_dosen()
    elif(selected_menu == "5"):
        search_dosen()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()


def show_dosen():
    clear_screen()
    data =[]
    contacts = []
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            contacts.append(row)

    if (len(contacts) > 0):
        labels = contacts.pop(0)
        print(f"{labels[0]} \t {labels[1]} \t\t {labels[2]}")
        print("-"*34)
        for data in contacts:
            print(data)
    else:
        print("Tidak ada data!")
    back_to_menu()


def create_dosen():
    clear_screen()
    with open(csv_filename, mode='a') as csv_file:
        fieldnames = ['NIP', 'NAMA', 'MATKUL']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        nip = input("Nip: ")
        nama = input("Nama lengkap: ")
        matkul = input("Mata Kuliah: ")

        writer.writerow({'NIP': nip, 'NAMA': nama, 'MATKUL': matkul})
        print("Berhasil disimpan!")

    back_to_menu()


def search_dosen():
    clear_screen()
    contacts = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            contacts.append(row)

    no = input("Cari berdasrakan Nip> ")

    data_found = []

    # mencari contact
    indeks = 0
    for data in contacts:
        if (data['NIP'] == no):
            data_found = contacts[indeks]
            
        indeks = indeks + 1

    if len(data_found) > 0:
        print("DATA DITEMUKAN: ")
        print(f"Nama: {data_found['NAMA']}")
        print(f"Matkul {data_found['MATKUL']}")
    else:
        print("Tidak ada data ditemukan")
    back_to_menu()
    


def edit_dosen():
    clear_screen()
    contacts = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            contacts.append(row)

    print("NIP \t NAMA \t\t MATKUL")
    print("-" * 32)

    for data in contacts:
        print(f"{data['NIP']} \t {data['NAMA']} \t {data['MATKUL']}")

    print("-----------------------")
    no = input("Pilih nomer Nip ")
    nama = input("nama baru: ")
    telepon = input("nomer nip baru: ")

    # mencari contact dan mengubah datanya
    # dengan data yang baru
    indeks = 0
    for data in contacts:
        if (data['NIP'] == no):
            contacts[indeks]['NAMA'] = nama
            contacts[indeks]['MATKUL'] = telepon
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['NIP', 'NAMA', 'MATKUL']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in contacts:
            writer.writerow({'NIP': new_data['NIP'], 'NAMA': new_data['NAMA'], 'MATKUL': new_data['MATKUL']}) 

    back_to_menu()



def delete_dosen():
    clear_screen()
    contacts = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            contacts.append(row)

    print("NIP \t NAMA \t\t MATKUL")
    print("-" * 32)

    for data in contacts:
        print(f"{data['NIP']} \t {data['NAMA']} \t {data['MATKUL']}")

    print("-----------------------")
    no = input("Hapus Nip ")

    # mencari contact dan mengubah datanya
    # dengan data yang baru
    indeks = 0
    for data in contacts:
        if (data['NIP'] == no):
            contacts.remove(contacts[indeks])
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['NIP', 'NAMA', 'MATKUL']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in contacts:
            writer.writerow({'NIP': new_data['NIP'], 'NAMA': new_data['NAMA'], 'MATKUL': new_data['MATKUL']}) 

    print("Data sudah terhapus")
    back_to_menu()

if __name__ == "__main__":
    while True:
        show_menu()