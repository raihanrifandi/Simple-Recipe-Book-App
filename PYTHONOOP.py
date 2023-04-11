import os

class Resep:
    def __init__(self, nama, bahan, instruksi, waktu): 
        self.nama = nama
        self.bahan = bahan
        self.instruksi = instruksi
        self.waktu = waktu
        
    # Menggunakan Fstring 
    def returnResep(self): # akan menampilkan resep yang baru saja ditambahkan oleh user
        os.system('cls')
        print(f"Resep {self.nama}")
        print("Bahan-bahan: ")
        for i in range(0, len(self.bahan)):
            print(self.bahan[i])
        print(f"\nLangkah-langkah: ")
        for i in range(0, len(self.instruksi)):
            print(self.instruksi[i])
        print(f"\nResep ini memerlukan waktu {self.waktu} menit\n")

class bukuResep():
    def __init__(self):
        self.arrayResep = []
        
    def memasukkanBahan(self): 
        try:
            jumlahBahan = int(input("Masukkan jumlah bahan: ")) 
            arrayBahan = list(map(str,input("Masukkan bahan-bahan: ").replace(" ", "").split(',', jumlahBahan))) [:jumlahBahan]
            # membuat list array dengan menggunakan function map() dan input dipisahkan oleh split()
            # strip(0) berfungsi untuk menghilangkan whitespace yang diikutsertakan oleh user saat proses penginputan
        except ValueError:
            print("Masukkan input berupa angka")
            return bukuResep.memasukkanBahan() # 
            # menggunakan rekursif sehingga input memasukkan bahan tidak berhenti
        else:
            return arrayBahan
    
    def memasukkanInstruksi(self):
        try:
            arrayInstruksi = []
            jumlahInstruksi = int(input("Masukkan jumlah langkah-langkah: "))
            for i in range (jumlahInstruksi):
                print("Langkah ke-", i+1)
                arrayInstruksi.append(str(input()))
        except ValueError:
            print("Masukkan input berupa angka")
            return bukuResep.memasukkanInstruksi()
        else:
            return arrayInstruksi
        
       
    # function untuk menambahkan resep
    def tambahResep(self, tambahMasakan):
        self.arrayResep.append(tambahMasakan)

    # function untuk menghapus resep
    def hapusResep(self, hapusMasakan):
        for i in range(len(self.arrayResep)):
            if self.arrayResep[i].nama.lower() == hapusMasakan.lower():
                self.arrayResep.remove(bukuResep.arrayResep[i])
                print(f"{hapusMasakan} telah dihapus dari buku resep\n")
                return
            else: 
                print(f"{hapusMasakan} Resep tidak dapat ditemukan\n")
                return

    # function untuk mengedit resep
    def editResep(self, edit):
        namaLama = input("Silahkan masukkan nama resep dari komponen yang ingin anda ganti: ")
        if edit == "nama":
            for i in range((len(self.arrayResep))):
                if self.arrayResep[i].nama.lower() == namaLama.lower():
                    namaBaru = input("Masukkan nama baru dari resep yang ingin anda ganti: ")
                    self.arrayResep[i].nama = namaBaru 
                    print("\n")
                    Resep.returnResep(bukuResep.Resep[i])
                    return
                else:
                    print("Resep tidak dapat ditemukan")
                    return
        elif edit == "bahan":
            for i in range(len(self.arrayResep)):
                if self.arrayResep[i].nama.lower() == namaLama.lower():
                    print("\n")
                    bahanSesudah = bukuResep.memasukkanBahan()
                    self.arrayResep[i].bahan = bahanSesudah
                    print("\n")
                    Resep.returnResep(bukuResep.arrayResep[i])
                    return
                else:
                    print("Resep tidak dapat ditemukan")
                    return
        elif edit == "instruksi":
            for i in range(len(self.arrayResep)):
                if self.arrayResep[i].nama.lower() == namaLama.lower():
                    print("\n")
                    instruksiBaru = bukuResep.memasukkanInstruksi()
                    self.arrayResep[i].instruksi = instruksiBaru
                    print("\n")
                    Resep.returnResep(bukuResep.arrayResep[i])
                    return
                else:
                    print("Resep tidak dapat ditemukan")
                    return
        elif edit == "waktu":
            for i in range(len(self.arrayResep)):
                if self.arrayResep[i].nama.lower() == namaLama.lower():
                    print("\n")
                    waktuSesudah = int(input("Berapa menit waktu baru yang dibutuhkan? "))
                    self.arrayResep[i].waktu = waktuSesudah
                    print("\n")
                    Resep.returnResep(bukuResep.arrayResep[i])
                    return
                else:
                    print("Resep tidak dapat ditemukan")
                    return
        else:
            print("Pilih komponen resep yang ingin anda ganti: nama, bahan, instruksi, waktu")
        
    # function untuk mencari resep
    def cariResep(self, pencarian):
        for i in range(len(self.arrayResep)):
            if self.arrayResep[i].nama.lower() == pencarian.lower():
                print("\n")
                Resep.returnResep(bukuResep.arrayResep[i])
                return
            else:
                print("Resep tidak dapat ditemukan\n")
                return

    # menampilkan resep yang telah ditambahkan
    def resepDitambahkan(self):
        for i in range(0, len(self.arrayResep)):
            print(self.arrayResep[i].nama)

# deklarasi variabel untuk menyimpan class
bukuResep = bukuResep()

# program utama
while True:
    # Membaca file untuk menampilkan header
    file = open("header.txt", "r")
    print(file.read())
    print("\nSelamat Datang di Dish-n-Dash! \n ================== \n |1. Tambah resep | \n |2. Hapus resep  | \n |3. Edit resep   | \n |4. Cari resep   | \n |6. Keluar       | \n ==================")
    print("\nResep yang baru saja anda tambahkan:")
    bukuResep.resepDitambahkan()
    answerChoice = input("Masukkan pilihan: ")
    if answerChoice == "1":
        os.system('cls')
        print("[1] TAMBAH RESEP")
        nama = input("Nama resep: ")
        bahan = bukuResep.memasukkanBahan()
        instruksi = bukuResep.memasukkanInstruksi()
        waktu = int(input("Lama waktu pembuatan: "))
        resepBaru = Resep(nama, bahan, instruksi, waktu)
        bukuResep.tambahResep(resepBaru)
        print("\n")
        resepBaru.returnResep()
    elif answerChoice == "2":
        os.system('cls')
        print(["[2] HAPUS RESEP"])
        hapusMasakan = str(input("Resep mana yang ingin anda hapus? "))
        bukuResep.hapusResep(hapusMasakan)
    elif answerChoice == "3":
        os.system('cls')
        print("[3] EDIT RESEP")
        editMasakan = str(input("Pilih komponen resep yang ingin anda gant \n [*]nama \n [*]bahan \n [*]instruksi \n [*]waktu \n "))
        bukuResep.editResep(editMasakan.lower())
    elif answerChoice == "4":
        os.system('cls')
        print("[4] CARI RESEP")
        cariMasakan = str(input("Pilih resep yang ingin anda cari: "))
        bukuResep.cariResep(cariMasakan)
    elif answerChoice == "5":
        break
    else:
        print("Silahkan pilih opsi dari 1-6")
