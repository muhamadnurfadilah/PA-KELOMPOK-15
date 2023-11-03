from prettytable import PrettyTable 
import json 
import pwinput 
import os 
os.system("cls")


#prettytable 
tabel_data = PrettyTable()
tabel_data.field_names = ["No","Kode", "Kategori", "Harga/Jam", "Status"]


#file json untuk menyimpan akun customer
json_login = "c:/Users/User/OneDrive/Semester 1/DDP/PA Semester 1/akun.json"
with open(json_login, "r") as akun_cust: 
    customer = json.load(akun_cust)


#file json untuk menyimpan produk
jsonproduk = open("c:/Users/User/OneDrive/Semester 1/DDP/PA Semester 1/produk.json")
data = json.loads(jsonproduk.read())


#variabel untuk mengakses dictio nary pada file json
username = customer.get("Nama")
pasword = customer.get("Password")
saldo = customer.get("E-Money")


#fungsi untuk menyimpan data setelah diubah
def simpan():
    with open("produk.json", "w") as sn:
        json.dump(data, sn, indent=4)

#login admin
def login_admin():
    print("\n+-----------------------------------------------------+")
    print("|                   LOGIN AKUN ADMIN                  |")
    print("+-----------------------------------------------------+")
    while True:
        try:
            nama = input(">> Username : ")
            pw = pwinput.pwinput(">> Password : ")
            if nama == "a" and pw == "12":
                print("\n                --- LOGIN BERHASIL ---           \n")
                return menu_admin()
                
            else:
                print("\n-> LOGIN ANDA GAGAL COBA LAGI ATAU KEMBALI")
                while True :
                    balik = input(">> Apakah anda ingin ke menu utama? (y/t) : ")
                    if balik == "y":
                        main_program()
                        break
                    elif balik == "t":
                        login_admin()
                        break
                    else :
                        print("\n-> PILIHAN TIDAK TERSEDIA")      
        except :
            print("\n-> PERHATIKAN INPUT")

#login customer
def login_customer():
    print("\n+-----------------------------------------------------+")
    print("|                 LOGIN AKUN CUSTOMER                 |")
    print("+-----------------------------------------------------+")
    while True :
        try :
            nama = input(">> Masukkan username Anda : ")
            password = pwinput.pwinput(">> Masukkan password Anda : ")
            global cari
            cari = username.index(nama)
            if nama == username[cari] and password == pasword[cari]:
                os.system("cls")
                print("\n                 --- LOGIN BERHASIL ---                \n")
                menu_customer2()
                break
            elif nama == username[cari] and password != pasword[cari]:
                print("\n-> PASSWORD YANG ANDA INPUT SALAH")
                print("-> MOHON UNTUK COBA LAGI\n")
                Lanjut = input(">> Apakah anda ingin kembali ke menu utama? (y/t) : ")
                if Lanjut == "y":
                    print()
                    menu_customer1()     
                elif Lanjut == "t":
                    print()
                    login_customer()
                    return
                else :
                    print("\n-> HANYA KETIK y/t")
                    login_customer()
                return
            elif nama != username[cari] and password == pasword[cari]:
                print("\n-> USERNAME YANG ANDA INPUT SALAH")
                print("\n-> MOHON UNTUK COBA LAGI\n")
                Lanjut = input(">> Apakah anda ingin kembali ke menu utama? (y/t) : ")
                if Lanjut == "y":
                    print()
                    menu_customer1()     
                elif Lanjut == "t":
                    login_customer()
                else :
                    print("\n-> HANYA KETIK y/t")
                    login_customer()
                return
        except ValueError:
            print("\n -> USERNAME BELUM TERDAFTAR")
            print(" -> MOHON UNTUK COBA LAGI\n")
            Lanjut = input(">> Apakah anda ingin kembali ke menu utama? (y/t) : ")
            if Lanjut == "y":
                print()
                menu_customer1()     
            elif Lanjut == "t":
                login_customer()
            else :
                print("\n-> HANYA KETIK y/t")
                login_customer()
            return

#registrasi customer
def registrasi_customer():
    print("\n+-----------------------------------------------------+")
    print("|              REGISTRASI AKUN CUSTOMER               |")
    print("+-----------------------------------------------------+")
    while True :
        try:
            nama = input(">> Masukkan username yang ingin dibuat : ")
            if nama == "":
                print("-> INPUT HARUS DI ISI")
                print("-> SILAKAN COBA LAGI!\n")
            elif all(x.isalpha() for x in nama):
                if nama in customer["Nama"]:
                    print("-> MAAF USERNAME TELAH TERDAFTAR\n")
                    while True :
                        print("+-----------------------------------------------------+")
                        print("|1. Login Akun                                        |")
                        print("|2. Registrasi Akun Baru                              |")
                        print("+-----------------------------------------------------+")
                        pilihan = input("Masukan pilihan anda : ")
                        if pilihan == "1":
                            login_customer()
                            break
                        elif pilihan == "2":
                            print("\n-> SILAHKAN REGISTRASI USERNAME YANG BARU")
                            registrasi_customer()
                        else :
                            print("\n-> PILIHAN TIDAK TERSEDIA\n")

                else:
                    password = pwinput.pwinput(">> Masukan password yang ingin dibuat : ")
                    if password == "":
                        print("-> INPUT HARUS DI ISI!")
                        print("-> MOHON MAAF COBA LAGI!\n")
                    elif all(x.isnumeric() for x in password):
                        saldo_emoney = 0
                        saldo.append(saldo_emoney)
                        username.append(nama)
                        pasword.append(password)
                        
                        with open(json_login, "w") as add_customer:
                            json.dump(customer, add_customer, indent=4)   
                        print("\n            --- REGISTRASI AKUN BERHASIL ---           \n")
                        login_customer()
                        break
                    else :
                        print("-> PASSWORD HARUS BERUPA ANGKA")
            else :
                print("-> USERNAME HANYA BERUPA HURUF")
        except :
            print("-> INPUT TIDAK VALID\n")


# CRUD admin
def create():
    read()
    print("\n      --- MENAMBAHKAN DATA RUANGAN BARU ---     \n")
    while True:
        try:
            kode = str(input(">> Kode = "))
            if kode in data["Kode"]:
                print("\n-> KODE TIDAK BOLEH DUPLIKAT\n")
            elif len(kode) == 3 and all(x.isdigit() for x in kode):
                break
            elif len(kode) == 2 and all(x.isdigit() for x in kode):
                print("\n-> KODE TIDAK BOLEH KURANG DARI 3 DIGIT\n")
            elif len(kode) == 1 and all(x.isdigit() for x in kode):
                print("\n-> KODE TIDAK BOLEH KURANG DARI 3 DIGIT\n")
            elif len(kode) > 3 and all(x.isdigit() for x in kode):
                print("\n-> KODE TIDAK BOLEH LEBIH DARI 3 DIGIT\n")
            elif len(kode) <= 0 and all(x.isdigit() for x in kode):
                print("\n-> KODE TIDAK BOLEH KOSONG\n")
            elif len(kode) > 0 and all(x.isalpha() for x in kode):
                print("\n-> KODE HARUS BERUPA ANGKA\n")
            elif len(kode) == "" and all(x.isspace() for x in kode):
                print("\n-> KODE TIDAK BOLEH KOSONG\n")
            else:
                print("\n-> INPUT YANG DIMASUKAN TIDAK SESUAI")
                print("-> SILAHKAN COBA LAGI\n")
        except :
            print("\n-> PERHATIKAN INPUT")

    while True:
        try :
            tambah = input(">> Kategori : ").capitalize()
            if tambah in data["Kategori"]:
                print("\n-> NAMA TIDAK BOLEH DUPLIKAT")
                cari_sewa = data.get("Kategori").index(tambah)
                data["Kategori"][cari_sewa] = data.get("Kategori")[cari_sewa] +1
                read()
            elif all(x.isspace () for x in tambah):
                print("\n-> INPUT TIDAK BOLEH KOSONG")
            elif all(x.isalpha() for x in tambah) and len(tambah) <= 20:
                break
            elif len(tambah) > 20:
                print("\n-> KATEGORI TIDAK BOLEH LEBIH DARI 20 HURUF\n")
            elif all(x.isnumeric() for x in tambah):
                print("\n-> INPUT TIDAK BOLEH ANGKA\n")
            else:
                print("\n-> INPUT YANG DIMASUKAN TIDAK SESUAI")
                print("-> SILAHKAN COBA LAGI\n")
        except :
            print("\n-> PERHATIKAN INPUT")

    while True:
        try:
            harga = int(input(">> Harga Sewa : Rp "))

            if harga < 0:
                print("\n-> HARGA TIDAK BOLEH KURANG DARI 0")
            elif harga == 0:
                print("\n-> HARGA HARUS LEBIH DARI 0")
            elif harga < 100000000 :
                break
            elif harga > 100000000 :
                print("\n-> HARGA SEWA TIDAO BOLEH LEBIH DARI 100000000\n")
            else:
                print("\n-> TOLONG MASUKAN INPUT YANG BENAR")
                print("-> SILAHKAN COBA LAGI\n")
        except ValueError:
            print("\n-> MASUKAN ANGKA")

    while True:
        try:
            status = "Kosong"
            print("Status: " + status)
            break
        except ValueError:
            print("\n-> INPUT TIDAK VALID")

    data["Kode"].append(kode)
    data["Kategori"].append(tambah)
    data["Harga Sewa"].append(harga)
    data["Status"].append(status)
    simpan()
    print("\n        --- DATA BERHASIL DITAMBAHKAN ---       \n")

def read():
    no = 1
    tabel_data.clear_rows()
    for i in range(len(data["Kategori"])):
        tabel_data.add_row(
            [
                no,
                (data["Kode"][i]),
                (data["Kategori"][i]),
                "Rp." + str(data["Harga Sewa"][i]),
                data["Status"][i],
            ]
        )
        no += 1
        simpan()

    print(tabel_data)

def update():
    print("\n          --- MEMPERBARUI DATA RUANGAN ---          \n")
    read()
    while True:
        try :
            nama_p = str(input(">> Masukkan kode yang ingin diperbarui : "))
            cari_n = data.get("Kode").index(nama_p)
            break
        except :
            print("\n-> KODE TIDAK DITEMUKAN")
            print("-> SILAHKAN COBA LAGI\n")
        
    while True :
        nm = input("\n>> Apakah anda ingin memperbarui kategori? (y/t) : ")
        if nm == "y":
            nub = input(">> Masukan kategori baru : ").capitalize()
            if nub in data["Kategori"] :
                print("\n-> KATEGORI SUDAH ADA")
                print("-> SILAHKAN MASUKAN KATEGORI YANG BERBEDA\n")
            elif all(x.isalpha() for x in nub) and len(nub) <= 10:
                data.get("Kategori")[cari_n] = nub
                print("\n          --- KATEGORI BERHASIL DIPERBARUI ---\n")
                break
            else :
                print("\n-> KATEGORI HANYA BOLEH ALPHABET")
                print("-> NAMA TIDAK BOLEH LEBIH DARI 10 HURUF\n")
        elif nm == "t":
            break
        else :
            print("\n-> PILIHAN TIDAK TERSEDIA")

    while True:
        hm = input("\n>> Apakah anda ingin memperbarui harga ? (y/t) : ")
        if hm == "y":
            while True :
                try :
                    hp_b = int(input(">> Masukkan harga baru : Rp. "))
                    if hp_b < 0:
                        print("\n-> HARGA TIDAK BOLEH KURANG DARI 0")
                    elif hp_b == 0:
                        print("\n-> HARGA HARUS LEBIH DARI 0")
                    elif hp_b > 0 and hp_b < 100000000:
                        data.get("Harga Sewa")[cari_n] = hp_b
                        print("\n          --- HARGA BERHASIL DIPERBARUI ---\n")
                        break
                    else :
                        print("\n->  HARGA TIDAK BISA LEBIH DARI 100000000")
                except :
                    print("\n-> PERHATIKAN INPUTAN")
            break
        elif hm == "t":
            break
        else :
            print("\n-> PILIHAN TIDAK TERSEDIA")
            
    simpan()
    read()
        

    while True :
        cd = input("\n>> Apakah anda ingin memperbarui status? (y/t) : ")
        if cd == "y":
            while True :
                piu = input(">> Masukan status baru (Terisi/Kosong) : ").capitalize
                if piu == "Terisi":
                    print("\n         --- KATEGORI BERHASIL DIUBAH ---\n")
                    break
                elif piu == "Kosong":
                    print("\n         --- KATEGORI BERHASIL DIUBAH ---\n")
                    break
                else :
                    print("\n-> STATUS HANYA BOLEH (Terisi) atau (Kosong)")
            break
        elif cd == "t":
            break
        else :
            print("\n-> PILIHAN TIDAK TERSEDIA")
            print("-> MASUKKAN INPUT YANG VALID\n")
    simpan()
    read()
    print("\n         --- DATA BERHASIL DIPERBARUI ---        \n")



def delete():
    read()
    print("\n         --- MENGHAPUS DATA RUANGAN ---        \n")
    while True:
        try:
            hapus_n = str(input(">> Masukan kode barang yang akan dihapus : "))
            if hapus_n == "" :
                print("\n-> INPUT TIDAK BOLEH KOSONG")
            elif hapus_n in data["Kode"]:
                cari_n = data.get("Kode").index(hapus_n)
                data.get("Kode").pop(cari_n)
                data.get("Kategori").pop(cari_n)
                data.get("Harga Sewa").pop(cari_n)
                data.get("Status").pop(cari_n)
                print("\n      --- DATA RUANGAN BERHASIL DIHAPUS ---\n")
            elif hapus_n not in data["Kode"]:
                print("\n       --- KODE TIDAK DITEMUKAN ----\n")

            simpan()
            read()
            break
        except:
            print("\n-> DATA TIDAK DITEMUKAN")
            print("-> SILAHKAN COBA LAGI\n")


def sewa_ruangan():
    while True: 
        try:
            print()
            read()
            simpan()
            sewa = input(">> Masukkan kategori ruangan yang ingin disewa : ").capitalize()
            if sewa in data["Kategori"]:
                cari_sewa = data.get("Kategori").index(sewa)

                if data["Status"][cari_sewa] == "Kosong":
                    durasi = int(input(">> Masukkan durasi sewa ruangan (/jam) : "))
                    if 0 < durasi < 100:
                        if data["Status"][cari_sewa] == "Kosong":
                            cari_kode = data.get("Kode")[cari_sewa]
                            cari_biaya = data.get("Harga Sewa")[cari_sewa]
                            total_sewa = cari_biaya * durasi

                            pembayaran(sewa, cari_sewa, durasi, total_sewa, cari_kode, cari_biaya)
                            
                        else: 
                            print("\n-> RUANGAN SUDAH TERISI")
                    else:
                        print("\n-> MASUKKAN DURASI SESUAI HITUNGAN JAM")
                        print("-> SILAKAN COBA LAGI\n")
                else:
                    print("\n-> RUANGAN SUDAH TERISI")
                    print("-> SILAKAN COBA KATEGORI YANG LAIN\n")
                    pass
            else: 
                print("\n-> KATEGORI TIDAK DITEMUKAN")
            
            while True:
                sewa_lagi = input(">> Apakah ingin menyewa ruangan lagi? (y/t) : ")
                if sewa_lagi== "y":
                    print("\n-> SILAKAN SEWA RUANGAN LAGI")
                elif sewa_lagi == "t":
                    break
                else:
                    print("\n-> INPUT YANG DIMASUKKAN SALAH ")
        except ValueError:
            print("\n-> INPUT TIDAK VALID")
        break

def pembayaran(sewa, cari_sewa, durasi, total_sewa, cari_kode, cari_biaya):
    print(f">> Total pembayaran : Rp {total_sewa}")
    with open("invoice-transaksi.txt", "a") as invoice:
        print("+----------------PENYEWAAN RUANGAN-----------------+", file=invoice)
        print(f" Kategori ruangan    : {sewa}", file=invoice)
        print(f" Kode ruangan        : {cari_kode}", file=invoice)
        print(f" Durasi sewa ruangan : {durasi} jam", file=invoice)
        print(f" Biaya sewa ruangan  : Rp {cari_biaya}", file=invoice)
        print("", file=invoice)
        print(f" Total biaya sewa    : Rp {total_sewa}", file=invoice)
        print("+--------------------------------------------------+\n", file=invoice)
    print("\n           ---SILAKAN LAKUKAN PEMBAYARAN---             \n")


    print("+-----------------------------------------------------+")
    print("|                  METODE PEMBAYARAN                  |")
    print("+-----------------------------------------------------+")
    print("|1. Tunai                                             |")
    print("|2. E-Money                                           |")
    print("+-----------------------------------------------------+")
    while True :
        print(f">> Total pembayaran : Rp {total_sewa}")
        pilihan = int(input(">> Masukan metode pembayaran = "))
        if pilihan == 1:
            uang = int(input("\n>> Masukan nominal uang tunai = "))
            if uang >= total_sewa: 
                kembalian = uang - total_sewa
                with open("struk-pembayaran.txt", "a") as struk:
                    print("+-------------------STRUK PEMBELIAN--------------------+", file=struk)
                    print(f" Kategori ruangan    : {sewa}", file=struk)
                    print(f" Kode ruangan        : {cari_kode}", file=struk)
                    print(f" Durasi sewa ruangan : {durasi} jam", file=struk)
                    print(f" Biaya sewa ruangan  : Rp {cari_biaya}", file=struk)
                    print("", file=struk)
                    print(f" Total pembayaran    : Rp {total_sewa}", file=struk)
                    print(f" Uang                : Rp {uang}", file=struk )
                    print(f" Kembalian           : Rp {kembalian}", file=struk)
                    print("+-----------------------------------------------------+\n", file=struk)
                    data.get("Status")[cari_sewa] = "Terisi"
                    print("\n             ---PEMBAYARAN BERHASIL---               \n")           

            elif uang < total_sewa: 
                uang_kurang = total_sewa - uang
                print(f">> Uang tunai kurang sebesar Rp {uang_kurang}")
                print("\n                 ---PEMBAYARAN GAGAL---                 \n")

        elif pilihan == 2:
            cari_saldo = customer.get("E-Money")[cari]
            if cari_saldo >= total_sewa:
                cari_saldo = customer["E-Money"][cari] - total_sewa
                with open("struk-pembayaran.txt", "a") as struk:
                    print("+-------------------STRUK PEMBELIAN--------------------+", file=struk)
                    print(f" Kategori ruangan    : {sewa}", file=struk)
                    print(f" Kode ruangan        : {cari_kode}", file=struk)
                    print(f" Durasi sewa ruangan : {durasi} jam", file=struk)
                    print(f" Biaya sewa ruangan  : Rp {cari_biaya}", file=struk)
                    print("", file=struk)
                    print(f" Total pembayaran    : Rp {total_sewa}", file=struk)
                    print(f" E-Money             : Rp {cari_saldo}", file=struk )
                    print("+-----------------------------------------------------+\n", file=struk)
                    data.get("Status")[cari_sewa] = "Terisi"
                    print("\n             ---PEMBAYARAN BERHASIL---               \n")           
                    break
            
            elif cari_saldo < total_sewa:
                saldo_kurang = total_sewa - cari_saldo
                print(f">> Uang tunai kurang sebesar Rp {saldo_kurang}")
                print("\n                 ---PEMBAYARAN GAGAL---                 \n")
                while True: 
                    topup = input("Apakah ingin top up E-Money? (y/t) : ")
                    if topup == "y":
                        os.system("cls")
                        topup_emoney()
                        break
                            
                    elif topup == "t":
                        print("\n             ---SALDO E-MONEY TIDAK CUKUP---            ")    
                        print("                 ---PEMBAYARAN GAGAL---                 \n")
                        break

                    else:
                        print("\n-> INPUT TIDAK VALID\n")  

            else:
                print("\n-> INPUT TIDAK VALID")    
        else:
            print("\n-> PILIIHAN TIDAK TERSEDIA")
            print("\n-> SILAKAN COBA LAGI\n")
            simpan()
        break

def topup_emoney():
    while True :
            print("+-----------------------------------------------------+")
            print("|                   TOP UP E-MONEY                    |")
            print("+-----------------------------------------------------+")
            print("|1. Rp 100.000                                        |")
            print("|2. Rp 200.000                                        |")
            print("|3. Rp 300.000                                        |")
            print("|4. Rp 400.000                                        |")
            print("|5. RP 500.000                                        |")
            print("+-----------------------------------------------------+")
            topup = int(input("\n>> Masukkan pilihan top up e-money : "))
            if topup == 1:
                customer.get("E-Money")[cari] = customer["E-Money"][cari] + 100000
                cari_saldo = customer.get("E-Money")[cari]
                print("\n+-----------------------------------------------------+")
                print(f"Saldo E-Money berhasil ditambah Rp {100000}")
                print(f"Saldo E-Money sekarang Rp {cari_saldo}")
                print("+-----------------------------------------------------+\n")
                print("            ---TOP UP E-MONEY BERHASIL---              \n")
                break

            elif topup == 2:
                customer.get("E-Money")[cari] = customer["E-Money"][cari] + 200000
                cari_saldo = customer.get("E-Money")[cari]
                print("\n+-----------------------------------------------------+")
                print(f"Saldo E-Money berhasil ditambah Rp {200000}")
                print(f"Saldo E-Money sekarang Rp {cari_saldo}")
                print("+-----------------------------------------------------+\n")
                print("            ---TOP UP E-MONEY BERHASIL---              \n")
                break

            elif topup == 3:
                customer.get("E-Money")[cari] = customer["E-Money"][cari] + 300000
                cari_saldo = customer.get("E-Money")[cari]
                print("\n+-----------------------------------------------------+")
                print(f"Saldo E-Money berhasil ditambah Rp {300000}")
                print(f"Saldo E-Money sekarang Rp {cari_saldo}")
                print("+-----------------------------------------------------+\n")
                print("            ---TOP UP E-MONEY BERHASIL---              \n")
                break

            elif topup == 4:
                customer.get("E-Money")[cari] = customer["E-Money"][cari] + 400000
                cari_saldo = customer.get("E-Money")[cari]
                print("\n+-----------------------------------------------------+")
                print(f"Saldo E-Money berhasil ditambah Rp {400000}")
                print(f"Saldo E-Money sekarang Rp {cari_saldo}")
                print("+-----------------------------------------------------+\n")
                print("            ---TOP UP E-MONEY BERHASIL---              \n")
                break

            elif topup == 5:
                customer.get("E-Money")[cari] = customer["E-Money"][cari] + 500000
                cari_saldo = customer.get("E-Money")[cari]
                print("\n+-----------------------------------------------------+")
                print(f"Saldo E-Money berhasil ditambah Rp {500000}")
                print(f"Saldo E-Money sekarang Rp {cari_saldo}")
                print("+-----------------------------------------------------+\n")
                print("            ---TOP UP E-MONEY BERHASIL---              \n")
                break

            else:
                print("\n-> PILIHAN TIDAK TERSEDIA")
                print("SILAKAN COBA LAGI\n") 
                break
    with open(json_login, "w") as add_customer:
        json.dump(customer, add_customer, indent=4)  
        

def cek_saldo_emoney():
    cari_saldo = customer.get("E-Money")[cari]
    print("+-----------------------------------------------------+")
    print(f" Saldo E-Money saat ini : Rp {cari_saldo}")
    print("+-----------------------------------------------------+\n")

def menu_admin():
    while True:
        try :
            print("+-----------------------------------------------------+")
            print("|                     MENU ADMIN                      |")
            print("+-----------------------------------------------------+")
            print("|1. Tambah Ruangan                                    |")
            print("|2. Lihat Informasi Ruangan                           |")
            print("|3. Perbarui Informasi Ruangan                        |")
            print("|4. Hapus Ruangan                                     |")
            print("|5. Kembali                                           |")
            print("+-----------------------------------------------------+")
            menu = int(input(">> Masukan menu yang dipilih : "))
            if menu == 1:
                os.system("cls")
                while True:
                    create()
                    Lanjut = input(">> Apakah anda ingin menambahkan data lagi? (y/t) : ")
                    if Lanjut == "y":
                        print("\n-> SILAKAN TAMBAH DATA KEMBALI")
                    elif Lanjut == "t":
                        os.system('cls')
                        break
                    else :
                        print("\n-> INPUT TIDAK VALID")
                    
            elif menu == 2:
                os.system("cls")
                while True :
                    read()
                    Lanjut = input(">> Apakah anda ingin kembali ke menu admin? (y/t) : ")
                    if Lanjut == "y":
                        os.system('cls')
                        break
                    elif Lanjut == "t":
                        print("\n        --- MENAMPILKAN DATA ---   \n")
                    else :
                        print("\n-> INPUT TIDAK VALID")

            elif menu == 3:
                os.system("cls")
                while True:
                    update()
                    Lanjut = input(">> Apakah anda ingin mengubah data lagi? (y/t) : ")
                    if Lanjut == "y":
                        print("\n-> SILAKAN UPDATE DATA LAGI")
                    elif Lanjut == "t":
                        os.system('cls')
                        break
                    else :
                        print("\n-> INPUT TIDAK VALID")

            elif menu == 4:
                os.system("cls")
                while True:
                    delete()
                    Lanjut = input(">> Apakah anda ingin menghapus data lagi? (y/t) : ")
                    if Lanjut == "y":
                        print("\n-> SILAKAN HAPUS DATA LAGI")
                    elif Lanjut == "t":
                        os.system('cls')
                        break
                    else :
                        print("\n-> INPUT TIDAK VALID")

            elif menu == 5:  # Opsi "Back" di menu admin
                os.system("cls")
                break

            else:
                print("\n-> PILIHAN TIDAK TERSEDIA")
                print("-> SILAHKAN COBA LAGI\n")
                menu_admin()
                break

        except ValueError:
            print("\n-> TOLONG MASUKAN INPUT DENGAN BENAR")
            print("-> SILAHKAN COBA LAGI\n")

        except KeyboardInterrupt:
            print("\n-> MOHON PERHATIKAN INPUT")

def menu_customer1():
    while True :
        try :
            print("+-----------------------------------------------------+")
            print("|                    MENU CUSTOMER                    |")
            print("+-----------------------------------------------------+")
            print("|1. Login                                             |")
            print("|2. Registrasi                                        |")
            print("|3. Kembali ke Menu Utama                             |")                  
            print("+-----------------------------------------------------+")
            menu = int(input(">> Masukkan menu yang dipilih : "))
            if menu == 1:
                os.system("cls")
                login_customer()

            elif menu == 2:
                os.system("cls")
                registrasi_customer()

            elif menu == 3:
                os.system("cls")
                break

            else:
                print("\n-> INPUT TIDAK VALID")
                print("-> SILAKAN COBA LAGI\n")
                break
                
        except ValueError:
            print("\n-> MOHON PERHATIKAN INPUT")
            print("-> INPUT HARUS ANGKA\n")  

        except KeyboardInterrupt:
            print("\n-> MOHON PERHATIKAN INPUT")

def menu_customer2():
    try:
        while True:
            print("+-----------------------------------------------------+")
            print("|                    MENU CUSTOMER                    |")
            print("+-----------------------------------------------------+")
            print("|1. Sewa Ruangan                                      |")
            print("|2. Top Up E-Money                                    |")
            print("|3. Cek Saldo E-Money                                 |") 
            print("|4. Kembali ke Menu Utama                             |")                 
            print("+-----------------------------------------------------+")
            pilihan = int(input(">> Masukkan pilihan = "))
            if pilihan == 1:
                os.system("cls")
                sewa_ruangan()

            elif pilihan == 2:
                os.system("cls")
                topup_emoney()

            elif pilihan == 3:
                os.system("cls")
                cek_saldo_emoney()

            elif pilihan == 4:
                os.system("cls")
                break

            else:
                print("\n-> PILIHAN TIDAK TERSEDIA")
                print("-> SILAKAN COBA LAGI")
                break

    except ValueError:
        print("\n-> INI BALIK KE MENU AWAL")

    except KeyboardInterrupt:
        print("\n-> MOHON PERHATIKAN INPUT")
    


#Tampilan Awal
def main_program():
    print("\n             SELAMAT DATANG DI ROOM & SPACE             ")   
    print("               Penyewaan Ruang Terpercaya               ")
    while True :
        try :
            print()
            print("+-----------------------------------------------------+")
            print("|                      MENU UTAMA                     |")
            print("+-----------------------------------------------------+")
            print("|1. Admin                                             |")
            print("|2. Customer                                          |")
            print("|3. Selesai                                           |")                  
            print("+-----------------------------------------------------+")
            menu = int(input(">> Masukan menu yang dipilih : "))
            os.system("cls")
            if menu == 1:
                print("--------------- ANDA MASUK KE MENU ADMIN --------------\n")
                login_admin()

            elif menu == 2:
                print("------------- ANDA MASUK KE MENU CUSTOMER -------------\n")
                menu_customer1()

            elif menu == 3:
                print("\n---------------- PROGRAM TELAH SELESAI ----------------")
                print("--------------------- TERIMA KASIH --------------------\n")
                break

            else:
                print("PILIHAN TIDAK TERSEDIA")
                print("-> SILAHKAN COBA LAGI")

        except KeyboardInterrupt:
            print("\n-> PERHATIKAN INPUT\n")
        except EOFError:
            print("\n-> PERHATIKAN INPUT\n")
        except ValueError:
            print("\n-> PERHATIKAN INPUT\n")

main_program()