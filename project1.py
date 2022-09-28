
perpustakaan = [
    {
        "nama_penulis" : "Osamu Dazai",
        "judul_buku" : "Gagal Menjadi Manusia",
        "tahun_terbit" : 1948,
        "jenis_buku" : "Novel",
        "harga" : 20000,
        "jml_buku_tersedia" : 30
    },
    {
        "nama_penulis" : "Eka Kurniawan",
        "judul_buku" : "Cantik itu Luka",
        "tahun_terbit" : 2002,
        "jenis_buku" : "Novel",
        "harga" : 23000,
        "jml_buku_tersedia" : 12
    },
    {
        "nama_penulis" : "Tere Liye",
        "judul_buku" : "Negeri Para Bedebah",
        "tahun_terbit" : 2012,
        "jenis_buku" : "Novel",
        "harga" : 18000,
        "jml_buku_tersedia" : 16
    },
    {
        "nama_penulis" : "Ahmad Fuadi",
        "judul_buku" : "Negeri 5 Menara",
        "tahun_terbit" : 2009,
        "jenis_buku" : "Novel",
        "harga" : 20000,
        "jml_buku_tersedia" : 14
    },
    {
        "nama_penulis" : "Ahmad Tohari",
        "judul_buku" : "Ronggeng Dukuh Paruk",
        "tahun_terbit" : 1982,
        "jenis_buku" : "Novel",
        "harga" : 21000,
        "jml_buku_tersedia" : 20
        

    }
]

rak = []
# Menu Utama
while True :
    pilihanMenu = input('''
    Selamat Datang di Perpusakaan Peminjaman Buku Digital
    
    List Menu :
    1. Menampilkan Daftar Buku
    2. Menambah Data Buku 
    3. Menghapus Data Buku
    4. Pinjam Buku
    5. Exit Program
    
    Masukkan angka menu yang ingin dijalankan [1 - 5] : ''')

    if(pilihanMenu == '1') :
        while True:
            pilihanMenu1 = input('''
            1. Tampilkan Seluruh Data Buku yang Tersedia
            2. Tampilkan Data Buku Tertentu
            3. Kembali ke Menu Utama
            Silahkan Pilih Sub Menu Read Data [1 - 3] : ''' )
            if(pilihanMenu1 == '1') :
                print('SELAMAT DATANG\n \t DI PERPUSTAKAAN PEMINJAMAN BUKU')
                print("------------------------------------------------------------------------------------------------------------------------------------------")
                print('Index\t|       Judul Buku \t      |     Nama Penulis     | Tahun \t     | Jenis  \t| Harga sewa/2 Bulan \t  |Jumlah Buku Tersedia  |')
                print("-----------------------------------------------------------------------------------------------------------------------------------------|")
                for i in range(len(perpustakaan)) :
                    print(' {}\t| {}\t      |   {}\t     | {}  \t     | {}\t|{} \t                  | {}                   |'.format(i,perpustakaan[i]["judul_buku"],perpustakaan[i]["nama_penulis"],perpustakaan[i]["tahun_terbit"],perpustakaan[i]["jenis_buku"],perpustakaan[i]["harga"],perpustakaan[i]["jml_buku_tersedia"]))
            if (pilihanMenu1 == '2') :
                ix = int(input("Masukan index yang ingin di tampilkan : "))
                if (ix < len(perpustakaan)) :
                    print('\nBerikut Merupakan Data Buku Sesuai Dengan Index Yang Dipilih')
                    print("------------------------------------------------------------------------------------------------------------------------------------------")
                    print('Index\t|       Judul Buku \t      |     Nama Penulis     | Tahun \t     | Jenis  \t| Harga sewa/2 Bulan \t  |Jumlah Buku Tersedia  |')
                    print("-----------------------------------------------------------------------------------------------------------------------------------------|")
                    print('{}\t| {}\t      |   {}\t     | {}  \t     | {}\t|{} \t                  | {}                   |'.format(ix,perpustakaan[ix]["judul_buku"],perpustakaan[ix]["nama_penulis"],perpustakaan[ix]["tahun_terbit"],perpustakaan[ix]["jenis_buku"],perpustakaan[ix]["harga"],perpustakaan[ix]["jml_buku_tersedia"]))
            if (pilihanMenu1 == '3') :
                break
            else :
                print("\n\tSilahkan masukkan kembali menu yang ingin ditampilkan")

# Add Data
    elif(pilihanMenu == '2') :
        while True:
            pilihanMenu2 = input('''
            1. Tambahkan Data Buku Baru
            2. Kembali ke Menu Utama
            Silahkan Pilih Sub Menu Read Data [1 - 2] : ''' )
            if(pilihanMenu2 == '1') :
                judulBuku = input("Masukkan Judul Buku : ")
                penulis = input("Masukkan Nama Penulis : ")
                tahun = input("Masukkan Tahun Buku : ")
                jenis = input("Masukkan Jenis Buku : ")
                hargaBuku = int(input("Masukkan harga sewa : "))
                stock = int(input("Masukkan Stock Buku : "))
                makeSure = input("Apakah anda yakin data akan ditambahkan? (y / n) : ")
                while True :
                    if(makeSure == 'y'):
                        perpustakaan.append({
                            "judul_buku" : judulBuku,
                            "nama_penulis" : penulis,
                            "tahun_terbit" : tahun,
                            "jenis_buku" : jenis,
                            "harga" : hargaBuku,
                            "jml_buku_tersedia" : stock
                            })
                    ("\n\t=====Data Buku Baru Telah Ditambahkan=====")
                    print("------------------------------------------------------------------------------------------------------------------------------------------")
                    print('Index\t|       Judul Buku \t      |     Nama Penulis     | Tahun \t     | Jenis  \t| Harga sewa/2 Bulan \t  |Jumlah Buku Tersedia  |')
                    print("-----------------------------------------------------------------------------------------------------------------------------------------|")
                    for i in range(len(perpustakaan)) :
                        print(' {}\t| {}\t      |   {}\t     | {}  \t     | {}\t|{} \t                  | {}                   |'.format(i,perpustakaan[i]["judul_buku"],perpustakaan[i]["nama_penulis"],perpustakaan[i]["tahun_terbit"],perpustakaan[i]["jenis_buku"],perpustakaan[i]["harga"],perpustakaan[i]["jml_buku_tersedia"]))
                    break
            elif(makeSure == 'n'):
                break
            if (pilihanMenu2 == '2') :
                break

# Delete Data

    elif(pilihanMenu == '3') :
        while True :
            pilihanMenu3 = input('''
            1. Hapus Data Buku 
            2. Kembali ke Menu Utama
            Silahkan Pilih Sub Menu Read Data [1 - 2] : ''' )
            if(pilihanMenu3 == '1') :
                print("------------------------------------------------------------------------------------------------------------------------------------------")
                print('Index\t|       Judul Buku \t      |     Nama Penulis     | Tahun \t     | Jenis  \t| Harga sewa/2 Bulan \t  |Jumlah Buku Tersedia  |')
                print("-----------------------------------------------------------------------------------------------------------------------------------------|") 
                for i in range(len(perpustakaan)) :
                    print(' {}\t| {}\t      |   {}\t     | {}  \t     | {}\t|{} \t                  | {}                   |'.format(i,perpustakaan[i]["judul_buku"],perpustakaan[i]["nama_penulis"],perpustakaan[i]["tahun_terbit"],perpustakaan[i]["jenis_buku"],perpustakaan[i]["harga"],perpustakaan[i]["jml_buku_tersedia"]))
                delBook = int(input('Masukkan index buku yang ingin dihapus : '))
                makeSure2 = input("Apakah anda yakin data akan dihapus? (y / n) : ")
                while True :
                    if(makeSure2 == 'y'):
                        del perpustakaan[delBook]
                        print("------------------------------------------------------------------------------------------------------------------------------------------")
                        print('Index\t|       Judul Buku \t      |     Nama Penulis     | Tahun \t     | Jenis  \t| Harga sewa/2 Bulan \t  |Jumlah Buku Tersedia  |')
                        print("-----------------------------------------------------------------------------------------------------------------------------------------|") 
                        for i in range(len(perpustakaan)) :
                            print(' {}\t| {}\t      |   {}\t     | {}  \t     | {}\t|{} \t                  | {}                   |'.format(i,perpustakaan[i]["judul_buku"],perpustakaan[i]["nama_penulis"],perpustakaan[i]["tahun_terbit"],perpustakaan[i]["jenis_buku"],perpustakaan[i]["harga"],perpustakaan[i]["jml_buku_tersedia"]))
                        print("\n\t\t =====Data Buku Berhasil Dihapus!=====")
                    break
            elif(makeSure2 == 'n'):
                    break
            if (pilihanMenu3 == '2') :
                break 


# Meminjam Buku

    elif(pilihanMenu == '4') :
        print("\t\t\t\t\t Daftar Buku")
        print("------------------------------------------------------------------------------------------------------------------------------------------")
        print('Index\t|       Judul Buku \t      |     Nama Penulis     | Tahun \t     | Jenis  \t| Harga sewa/2 Bulan \t  |Jumlah Buku Tersedia  |')
        print("-----------------------------------------------------------------------------------------------------------------------------------------|")
        for i in range(len(perpustakaan)) :
            print(' {}\t| {}\t      |   {}\t     | {}  \t     | {}\t|{} \t                  | {}                   |'.format(i,perpustakaan[i]["judul_buku"],perpustakaan[i]["nama_penulis"],perpustakaan[i]["tahun_terbit"],perpustakaan[i]["jenis_buku"],perpustakaan[i]["harga"],perpustakaan[i]["jml_buku_tersedia"]))
        while True  :
            indexBuku = int(input("Masukkan index buku yang ingin dipinjam : "))
            qtyBuku = int(input("Masukkan Jumlah Buku yang ingin Dipinjam : "))
            if(qtyBuku > perpustakaan[indexBuku]["jml_buku_tersedia"]) :
                print("Stock Buku Tidak Cukup")
            else :
                rak.append({
                    "judul" : perpustakaan[indexBuku]['judul_buku'],
                    "penulis" : perpustakaan[indexBuku]['nama_penulis'],
                    "harga1" : perpustakaan[indexBuku]['harga'],
                    "jml_buku" : perpustakaan[indexBuku]["jml_buku_tersedia"],
                    "indexBuku1" : indexBuku,
                    "qty" : qtyBuku
                })
            print("Isi Rak : ")
            print("\t\t\t\t\t Daftar Buku")
            print("------------------------------------------------------------------------------------------------------------------------------------------")
            print('Judul Buku \t      |     Nama Penulis   \t | Harga sewa/2 Bulan \t  |Jumlah Buku Tersedia  |')
            print("-----------------------------------------------------------------------------------------------------------------------------------------|")
            for item in rak :
                print(' {}\t| {}\t      |   {}\t     | {}  \t     |'.format(item["judul"],item["penulis"],item["harga1"],item["jml_buku"]))
            checker = input("Mau Pinjam Buku yang Lain? (y / n) : ")
            if(checker == 'n') :
                break

        print("\t\t\t\t\t Daftar Pinjaman Buku  : ")
        print("---------------------------------------------------------------------------------------------------------")
        print('Judul Buku \t      |     Nama Penulis \t   |     Quantity \t | Harga \t |    Total Harga Peminjaman Buku')
        print("---------------------------------------------------------------------------------------------------------|")
        totalHarga = 0
        for item in rak :
           print(' {}\t| {}\t      |   {}\t     | {}  \t   | {}   '.format(item["judul"],item["penulis"],item["qty"],item["harga1"],item["qty"] * item["harga1"]))
           totalHarga += item["indexBuku1"] * item["harga1"]
        while True :
            print("Total Yang Harus Dibayar = {}".format(totalHarga))
            jmluang = int(input('Masukkan Jumlah Uang : '))
            if (jmluang > totalHarga) :
                kembali = jmluang - totalHarga
                print("Terima Kasih  \n \n Uang Kembalian Anda : {} ".format(kembali))
                for item in rak :
                    perpustakaan[item["indexBuku1"]]["jml_buku_tersedia"] -= item["qty"]
                rak.clear()
                break
            elif(jmluang == totalHarga) :
                print("\t\t\nTerima Kasih")
                for item in rak :
                    perpustakaan[item["indexBuku1"]]["jml_buku_tersedia"] -= item["jml_buku"]
                rak.clear()
                break
            else :
                kekurangan = totalHarga - jmluang
                print('Uang Anda Kurang sebesar {}'.format(kekurangan))

# Exit

    elif(pilihanMenu == '5') :
        print("SELAMAT TINGGAL")
        break

 
