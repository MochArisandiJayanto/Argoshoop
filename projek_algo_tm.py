import os
import csv
import sys
import pandas as pd
from termcolor import cprint

csv_filename = 'akuns.csv'


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


cprint('''
                                                ------------------------------------
                                                |          selamat datang          |
                                                |           di agroshop            |           
                                                ------------------------------------
        '''.upper(), "blue")


def menu_akun():
    print("=== DATA AKUN ===")
    print("[1] Data Akun")
    print("[2] Edit Akun")
    print("[3] Hapus Akun")
    print("[99] kembali Menu Sebelumnya")
    print("[0] Logout")
    print("====================***NEXT***====================")
    selected_menu = int(input("Pilih menu> "))

    if (selected_menu == 1):
        show_akun()
    elif (selected_menu == 2):
        edit_akun()
    elif (selected_menu == 3):
        delete_akun()
    elif (selected_menu == 0):
        menu()
    elif (selected_menu == 99):
        menu_dua()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()


def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    menu_akun()


def show_akun():
    clear_screen()
    akun = []

    with open('akuns.csv', mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akun.append(row)

    email = input('Konfirmasi Email: ')
    password = input('Konfirmasi Password: ')

    data_found = []

    indeks = 0
    for data in akun:
        if (data['EMAIL'] == email and data['PASSWORD'] == password):
            data_found = akun[indeks]

        indeks = indeks + 1

    if len(data_found) > 0:
        print("Profil Akun: ")
        print(f"No: {data_found['NO']}")
        print(f"Nama: {data_found['NAMA']}")
        print(f"Saldo: {data_found['SALDO']}")
        print(f"Email: {data_found['EMAIL']}")
        print(f"Password: {data_found['PASSWORD']}")
    else:
        print("Data yang anda masukkan salah")
    back_to_menu()


def create_akun():
    print('\nCREATE ACCOUNT')
    print('[1] Lanjut membuat akun')
    print('[2] Login')
    pilih = int(input('Pilih menu: '))

    if pilih == 1:
        csvfile = open('akuns.csv')
        reader = csv.reader(csvfile)
        NO = int(input('No: '))
        # NO = str(NO)
        for row in reader:
            if row[0] == NO:
                same = True
                print("Same")
                break
            else:
                same = False
        if same == False:
            NAMA = str(input('Nama: '))
            SALDO = int(input('Saldo: '))

        csvfile = open('akuns.csv')
        readers = csv.reader(csvfile)
        EMAIL = str(input('Email: '))
        for row in readers:
            if row[3] == EMAIL:
                Same = True
                print("Same")
                break
            else:
                Same = False
        if Same == False:
            PASSWORD = str(input('Password: '))
            file = open('akuns.csv', 'a')
            info = '\n' + str(NO) + ',' + NAMA + ',' + \
                str(SALDO) + ',' + EMAIL + ',' + PASSWORD
            file.write(info)
            file.close()
        menu()
    elif pilih == 2:
        login()
    else:
        print('Menu yang anda pilih tidak tersedia.')
        create_akun()


def edit_akun():
    clear_screen()
    akuns = []

    with open('akuns.csv', mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akuns.append(row)

    print("====================***NEXT***====================")
    email = input("konfirmasi email: ")
    nama = input("nama baru: ")
    password = input("password terbaru: ")

    indeks = 0
    for data in akuns:
        if (data['EMAIL'] == email):
            akuns[indeks]['NAMA'] = nama
            akuns[indeks]['PASSWORD'] = password
        indeks = indeks + 1

    with open("akuns.csv", mode="w") as csv_file:
        fieldnames = ['NO', 'NAMA', 'SALDO', 'EMAIL', 'PASSWORD']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in akuns:
            writer.writerow({'NO': new_data['NO'], 'NAMA': new_data['NAMA'], 'SALDO': new_data['SALDO'],
                            'EMAIL': new_data['EMAIL'], 'PASSWORD': new_data['PASSWORD']})
        print("Sukses edit akun. \n")

    menu()


def delete_akun():
    clear_screen()
    akuns = []

    with open("akuns.csv", mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akuns.append(row)

    print("====================***NEXT***====================")
    email = input("konfirmasi email: ")
    password = input("konfirmasi password: ")
    benar = False
    # mencari contact dan mengubah datanya
    # dengan data yang baru
    indeks = 0
    for data in akuns:
        if (data['EMAIL'] == email and data['PASSWORD'] == password):
            benar = True
            akuns.remove(akuns[indeks])
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    if benar == True:
        with open("akuns.csv", mode="w") as csv_file:
            fieldnames = ['NO', 'NAMA', 'SALDO', 'EMAIL', 'PASSWORD']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for new_data in akuns:
                writer.writerow({'NO': new_data['NO'], 'NAMA': new_data['NAMA'], 'SALDO': new_data['SALDO'],
                                'EMAIL': new_data['EMAIL'], 'PASSWORD': new_data['PASSWORD']})

        print("Data sudah terhapus \n")
    else:
        print("Data yang anda masukkan salah \n")
        delete_akun()
    menu()


def login():
    clear_screen()
    akuns = []

    with open('akuns.csv', mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akuns.append(row)

    print("====================***NEXT***====================")
    email = input("Email: ")
    password = input("Password: ")

    indeks = 0
    for data in akuns:
        if (data['EMAIL'] == email and data['PASSWORD'] == password):
            menu_dua()
        indeks = indeks + 1
    print("Email dan Password yang anda masukkan salah. Silahkan masukkan ulang!\n")

    # correct_login_found = False

    # csvfile = open('akuns.csv')
    # reader = csv.reader(csvfile)
    # email = input("Email:")
    # password = input("Password:")

    # for row in reader:
    #     if row['EMAIL'] == email and row['PASSWORD'] == password:
    #         correct_login_found = True
    #         break

    # if correct_login_found == False:
    #     print("Bad login details")
    # else:
    #     menu_dua()

def menu():
    print("[1] Login")
    print("[2] Sign In")
    print("[3] Close Aplikasi")
    print("====================***NEXT***====================")
    selected = int(input("Pilih menu> "))

    if (selected == 1):
        login()
    elif (selected == 2):
        create_akun()
    elif (selected == 3):
        sys.exit()
    else:
        print("Menu yang anda pilih tidak tersedia\n")
        menu()


def menu_dua():
    clear_screen()
    print("[1] Akun")
    print("[2] Shopping")

    pilih = int(input("Pilih menu> "))

    if (pilih == 1):
        menu_akun()
    elif (pilih == 2):
        menu_barang()


csv_filename = 'produk.csv'


def menu_barang():
    print("=== MENU PRODUK ===")
    print("[1] Data Barang")
    print("[2] Beli Barang")
    print("[3] Tambah Barang")
    print("[0] Kembali Menu Sebelumnya")
    print("====================***NEXT***====================")
    selected_menu = int(input("Pilih menu> "))

    if (selected_menu == 1):
        show_barang()
    elif (selected_menu == 2):
        beli()
    elif (selected_menu == 3):
        tambahBarang()
    elif (selected_menu == 0):
        menu_dua()
    else:
        print("Kamu memilih menu yang salah!")


def back():
    print("\n")
    input("Tekan Enter untuk kembali...")
    menu_barang()


def show_barang():
    df = pd.read_csv(csv_filename)
    ab = list(df['NAMABARANG'])
    b = 0
    for a in range(len(ab)):
        b += 1
        print(f'{b}. {ab[a]}')
    print("====================***NEXT***====================")
    contacts = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            contacts.append(row)

    namaBarang = input("Ketik nama barang untuk melihat deskripsi:  ")
    title = namaBarang.title()

    data_found = []

    indeks = 0
    for data in contacts:
        if (data['NAMABARANG'] == title):
            data_found = contacts[indeks]

        indeks = indeks + 1

    if len(data_found) > 0:
        print(f'\n{namaBarang.upper()}')
        print(f"Nama Barang: {data_found['NAMABARANG']}")
        print(f"Berat: {data_found['BERAT']}")
        print(f"Harga: {data_found['HARGA']}")
        print(f"Deskripsi: {data_found['DESKRIPSI']}")
    else:
        print("Tidak ada data ditemukan")
    back()


def beli():
    df = pd.read_csv(csv_filename)
    ab = list(df['NAMABARANG'])
    b = 0
    for a in range(len(ab)):
        b += 1
        print(f'{b}. {ab[a]}')
    print("------------------------")

    belli = []
    barangBeli = []
    hargaBarang = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            belli.append(row)

    while True:
        masukan = input('Apakah anda ingin membeli?[y/n] ')

        if masukan == 'y' or masukan == 'Y':
            namaBarang = input("Ketik nama barang yang ingin dibeli:  ")
            title = namaBarang.title()

            data_found = []

            indeks = 0
            for data in belli:
                if (data['NAMABARANG'] == title):
                    data_found = belli[indeks]

                indeks = indeks + 1

            if len(data_found) > 0:
                barangBeli.append(title)
                hargaBarang.append(data_found['HARGA'])
            else:
                print("Tidak ada data ditemukan")
        elif masukan == 'n' or masukan == 'N':
            print("\nDETAIL PEMBELIAN")
            total = sum([int(i)
                        for i in hargaBarang if type(i) == int or i.isdigit()])
            total = int(total)
            for a in range(len(barangBeli)):
                print(barangBeli[a], '---> Rp', hargaBarang[a])
            print(f'Total Harga : Rp {total}')

            tanya = input("Apakah ingin melakukan pembayaran?[y/n] ")
            if tanya == 'y' or tanya == 'Y':
                csv_filesaldo = 'akuns.csv'

                akun = []

                with open(csv_filesaldo, mode="r") as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    for row in csv_reader:
                        akun.append(row)

                email = input('Konfirmasi Email: ')
                password = input('Konfirmasi Password: ')

                data_found = []

                indeks = 0
                for data in akun:
                    if (data['EMAIL'] == email and data['PASSWORD'] == password):
                        data_found = akun[indeks]

                    indeks = indeks + 1

                if len(data_found) > 0:
                    saldoSekarang = {data_found['SALDO']}
                    saldoSekarang = sum(
                        [int(i) for i in saldoSekarang if type(i) == int or i.isdigit()])
                else:
                    print("Data yang anda masukkan salah")

                yaa = []

                with open(csv_filesaldo, mode="r") as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    for row in csv_reader:
                        yaa.append(row)

                print("====================***NEXT***====================")
                email = input("konfirmasi email: ")
                password = input("konfirmasi password: ")
                saldo = saldoSekarang - total

                indeks = 0
                for data in yaa:
                    if (data['EMAIL'] == email and data['PASSWORD'] == password):
                        yaa[indeks]['SALDO'] = saldo
                    indeks = indeks + 1

                with open(csv_filesaldo, mode="w") as csv_file:
                    fieldnames = ['NO', 'NAMA','SALDO', 'EMAIL', 'PASSWORD']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in yaa:
                        writer.writerow({'NO': new_data['NO'], 'NAMA': new_data['NAMA'], 'SALDO': new_data['SALDO'],'EMAIL': new_data['EMAIL'], 'PASSWORD': new_data['PASSWORD']})
                    print("Saldo Anda Berkurang. Pembayaran Berhasil.")
                    break

            elif tanya == 'n' or tanya == 'N':
                continue
        else:
            print("Pilihan anda tidak tersedia.")

def tambahBarang():
    print("\nTambah Barang")
    csvfile = open('produk.csv')
    reader = csv.reader(csvfile)
    NAMABARANG = str(input('Nama Barang: '))
    NAMABARANG = NAMABARANG.title()
    for row in reader:
        if row[0] == NAMABARANG:
            same = True
            print("Same")
            tambahBarang()
        else:
            same = False
    if same == False:
        BERAT = str(input('Berat[1 Kg,2 Kg, etc]: '))
        HARGA = int(input('Harga[10000 or 25000 and etc]: '))
        DESKRIPSI = str(input('Deskripsi: '))

        file = open('produk.csv', 'a')
        info = '\n' + str(NAMABARANG) + ',' + BERAT + ',' + \
            str(HARGA) + ',' + DESKRIPSI + ','
        file.write(info)
        file.close()
        print("Tambah barang berhasil!")
    back()

if __name__ == "__main__":
    while True:
        menu()
