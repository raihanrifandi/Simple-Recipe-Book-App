import os

class Resep:
    def __init__(self, nama, bahan, instruksi, waktu):
        self.nama = nama
        self.bahan = bahan
        self.instruksi = instruksi
        self.waktu = waktu
        
    def lihat_resep(self):
        print("Nama resep:", self.nama)
        print("Bahan:", self.bahan)
        print("Cara memasak:")
        for langkah, langkah_masak in enumerate(self.instruksi, start=1):
            print(f"{langkah}. {langkah_masak}")
        print("Lama waktu:", self.waktu, "menit")
        print("="*50)

class BukuResep:
    def __init__(self):
        self.daftar_resep = []
        
    def tambah_resep(self, nama, bahan, instruksi, waktu):
        resep_baru = Resep(nama, bahan, instruksi, waktu)
        self.daftar_resep.append(resep_baru)
        
    def edit_resep(self, nama):
        indeks_resep = None
        for i, resep in enumerate(self.daftar_resep):
            if resep.nama.lower() == nama.lower():
                indeks_resep = i
                break
        if indeks_resep is None:
            print("Resep tidak dapat ditemukan!")
            return

        print(f"Nama resep: {self.daftar_resep[indeks_resep].nama}")
        print(f"Bahan: {self.daftar_resep[indeks_resep].bahan}")
        print(f"Lnagkah-langkah:")
        
        for langkah, langkah_masak in enumerate(self.daftar_resep[indeks_resep].instruksi, start=1):
            print(f"{langkah}. {langkah_masak}")
            
        print(f"Lama waktu: {self.daftar_resep[indeks_resep].waktu} menit")
        print("=" * 50)

        pilihan_edit = input("Pilih komponen resep yang ingin anda edit (1-4): \n"
                             "1. Nama resep\n"
                             "2. Bahan\n"
                             "3. Langkah-langkah\n"
                             "4. Lama waktu\n")
        
        if pilihan_edit == "1":
            nama_baru = input("Masukkan nama resep yang baru: ")
            self.daftar_resep[indeks_resep].nama = nama_baru
            print("[STATUS]\nNama resep berhasil diubah")
            
        elif pilihan_edit == "2":
            bahan_baru = input("Masukkan bahan-bahan yang baru (Input dipisahkan dengan koma): ")
            self.daftar_resep[indeks_resep].bahan = bahan_baru.split(", ")
            print("[STATUS]\nBerhasil diubah")
            
        elif pilihan_edit == "3":
            arrayInstruksi_baru = []
            while True:
                instruksi_baru = input("Masukkan cara memasak baru (kosongkan jika sudah selesai): ")
                if instruksi_baru == "":
                    break
                arrayInstruksi_baru.append(instruksi_baru)
            self.daftar_resep[indeks_resep].instruksi = arrayInstruksi_baru
            print("[STATUS]\nLangkah-langkah berhasil diubah")
            
        elif pilihan_edit == "4":
            waktu_baru = int(input("Masukkan lama wakt yang baru (dalam menit): "))
            self.daftar_resep[indeks_resep].waktu = waktu_baru
            print("[STATUS]Lama waktu berhasil diubah")
            
        else:
            print("Silahkan masukkan input sesuai dengan angka pada menu")

    def hapus_resep(self, nama):
        ketemu = False
        for i, resep in enumerate(self.daftar_resep):
            if resep.nama.lower() == nama.lower():
                self.daftar_resep.pop(i)
                print(f"Resep '{nama}' berhasil dihapus")
                ketemu = True
                break
        if not ketemu:
            print("Resep tidak dapat ditemukan!")
                
    def cari_resep(self, kata_kunci):
        hasil_pencarian = []
        for resep in self.daftar_resep:
            if kata_kunci.lower() in resep.nama.lower():
                hasil_pencarian.append(resep)
        return hasil_pencarian
    
    def lihat_semua_resep(self):
        for resep in self.daftar_resep:
            resep.lihat_resep()

# Program utama
buku_resep = BukuResep()
os.system('cls')
file = open("header.txt", "r")
print(file.read())

while True:
    print("\nSelamat Datang di Dish-n-Dash!")
    print("[1] Tambah resep")
    print("[2] Edit resep")
    print("[3] Hapus resep")
    print("[4] Cari resep")
    print("[5] Lihat daftar resep")
    print("[6] Keluar")
    pilihan = input("Masukkan pilihan menu: ")
    
    if pilihan == "1":
        os.system('cls')
        nama = input("Masukkan nama resep: ")
        bahan = input("Masukkan bahan-bahan (dipisahkan dengan koma): ")
        bahan = bahan.split(", ")
        instruksi = []
        while True:
            langkah_masak = input("Masukkan langkah-langkah (kosongkan jika sudah selesai): ")
            if langkah_masak == "":
                break
            instruksi.append(langkah_masak)
        while True:
            try:
                waktu = int(input("Masukkan lama waktu untuk membuat resep ini (dalam menit): "))
            except ValueError:
                print("[PERINGATAN]Masukkan input berupa angka dalam menit")
            else:
                break
        buku_resep.tambah_resep(nama, bahan, instruksi, waktu)
        os.system('cls')
        print("[STATUS]\nResep berhasil ditambahkan ke dalam list!")
            
    elif pilihan == "2":
        os.system('cls')
        nama = input("Masukkan nama resep yang ingin anda ubah: ")
        buku_resep.edit_resep(nama)
    
    elif pilihan == "3":
        os.system('cls')
        nama = input("Masukkan nama resep yang ingin anda hapus: ")
        buku_resep.hapus_resep(nama)
        
    elif pilihan == "4":
        os.system('cls')
        kata_kunci = input("Masukkan kata kunci: ")
        hasil_pencarian = buku_resep.cari_resep(kata_kunci)
        if hasil_pencarian:
            print("Hasil pencarian:")
            for resep in hasil_pencarian:
                print("Nama resep:", resep.nama)
                print("Bahan:", resep.bahan)
                print("Langkah-langkah: ")
                for i in range(0, len(resep.instruksi)):
                    print(f"{i+1}. {resep.instruksi[i]}")
                print("Lama waktu:", resep.waktu, "menit")
                print("="*50)
        else:
            print("[STATUS]\nResep tidak dapat ditemukan!")
            
    elif pilihan == "5":
        buku_resep.lihat_semua_resep()
        
    elif pilihan == "6":
        break
    
    else:
        print("Input yang anda masukkan tidak sesuai, silahkan coba lagi")
