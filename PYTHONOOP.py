import os

class Resep:
    def __init__(self, nama_resep, bahan, cara_masak, lama_membuat):
        self.nama_resep = nama_resep
        self.bahan = bahan
        self.cara_masak = cara_masak
        self.lama_membuat = lama_membuat
        
    def lihat_resep(self):
        print("Nama resep:", self.nama_resep)
        print("Bahan:", self.bahan)
        print("Cara memasak:")
        for langkah, langkah_masak in enumerate(self.cara_masak, start=1):
            print(f"{langkah}. {langkah_masak}")
        print("Lama membuat:", self.lama_membuat, "menit")
        print("="*50)

class BukuResep:
    def __init__(self):
        self.daftar_resep = []
        
    def tambah_resep(self, nama_resep, bahan, cara_masak, lama_membuat):
        resep_baru = Resep(nama_resep, bahan, cara_masak, lama_membuat)
        self.daftar_resep.append(resep_baru)
        
    def edit_resep(self, nama_resep):
        for resep in self.daftar_resep:
            if resep.nama_resep.lower() == nama_resep.lower():
                print(f"Nama resep: {resep.nama_resep}")
                print(f"Bahan: {resep.bahan}")
                print(f"Cara memasak:")
                for langkah, langkah_masak in enumerate(resep.cara_masak, start=1):
                    print(f"{langkah}. {langkah_masak}")
                print(f"Lama membuat: {resep.lama_membuat} menit")
                print("="*50)
                pilihan_edit = input("Pilih bagian yang ingin diedit (1-4): \n"
                                     "1. Nama resep\n"
                                     "2. Bahan\n"
                                     "3. Cara memasak\n"
                                     "4. Lama membuat\n")
                if pilihan_edit == "1":
                    nama_resep_baru = input("Masukkan nama resep baru: ")
                    resep.nama_resep = nama_resep_baru
                    print("[STATUS]\nNama resep berhasil diubah")
                elif pilihan_edit == "2":
                    bahan_baru = input("Masukkan bahan-bahan baru (dipisahkan dengan koma): ")
                    resep.bahan = bahan_baru.split(", ")
                    print("[STATUS]\nBahan berhasil diubah")
                elif pilihan_edit == "3":
                    cara_masak_baru = []
                    while True:
                        langkah_masak_baru = input("Masukkan cara memasak baru (kosongkan jika sudah selesai): ")
                        if langkah_masak_baru == "":
                            break
                        cara_masak_baru.append(langkah_masak_baru)
                    resep.cara_masak = cara_masak_baru
                    print("[STATUS]\nCara memasak berhasil diubah")
                elif pilihan_edit == "4":
                    lama_membuat_baru = input("Masukkan lama membuat baru (dalam menit): ")
                    resep.lama_membuat = lama_membuat_baru
                    print("[STATUS]\nLama membuat berhasil diubah")
                else:
                    print("Pilihan tidak valid")
                    break
            else:
                print("Resep tidak ditemukan!")
                return False
                
    def hapus_resep(self, nama_resep):
        for resep in self.daftar_resep:
            if resep.nama_resep.lower() == nama_resep.lower():
                self.daftar_resep.remove(resep)
                break
            else:
                print("Resep tidak ditemukan!")
                return False
                
    def cari_resep(self, kata_kunci):
        hasil_pencarian = []
        for resep in self.daftar_resep:
            if kata_kunci.lower() in resep.nama_resep.lower():
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
    print("[5] Lihat semua resep")
    print("[6] Keluar")
    pilihan = input("Masukkan pilihan menu: ")
    
    if pilihan == "1":
        os.system('cls')
        nama_resep = input("Masukkan nama resep: ")
        bahan = input("Masukkan bahan-bahan (dipisahkan dengan koma): ")
        bahan = bahan.split(", ")
        cara_masak = []
        while True:
            langkah_masak = input("Masukkan cara memasak (kosongkan jika sudah selesai): ")
            if langkah_masak == "":
                break
            cara_masak.append(langkah_masak)
        while True:
            try:
                lama_membuat = int(input("Masukkan lama memasak (dalam menit): "))
            except ValueError:
                print("[PERINGATAN]Masukkan input berupa angka dalam menit")
            else:
                break
        buku_resep.tambah_resep(nama_resep, bahan, cara_masak, lama_membuat)
        os.system('cls')
        print("[STATUS]\nResep berhasil ditambahkan!")
            
    elif pilihan == "2":
        os.system('cls')
        nama_resep = input("Masukkan nama resep yang ingin diubah: ")
        if buku_resep.edit_resep(nama_resep):
            print("[STATUS]\nResep berhasil diubah!")
        else:
            print("[STATUS]\nResep tidak berhasil diubah!")
            
    elif pilihan == "3":
        os.system('cls')
        nama_resep = input("Masukkan nama resep yang ingin dihapus: ")
        if buku_resep.hapus_resep(nama_resep):
            print("[STATUS]\nResep berhasil dihapus!")
        else:
            print("[STATUS]\nResep tidak berhasil dihapus!")
        
    elif pilihan == "4":
        os.system('cls')
        kata_kunci = input("Masukkan kata kunci: ")
        hasil_pencarian = buku_resep.cari_resep(kata_kunci)
        if hasil_pencarian:
            print("Hasil pencarian:")
            for resep in hasil_pencarian:
                print("Nama resep:", resep.nama_resep)
                print("Bahan:", resep.bahan)
                print("Cara membuat: ")
                for i in range(0, len(resep.cara_masak)):
                    print(f"{i+1}. {resep.cara_masak[i]}")
                print("Lama membuat:", resep.lama_membuat, "menit")
                print("="*50)
        else:
            print("[STATUS]\nResep tidak ditemukan!")
            
    elif pilihan == "5":
        buku_resep.lihat_semua_resep()
        
    elif pilihan == "6":
        break
    
    else:
        print("Menu tidak valid. Silakan coba lagi.")
