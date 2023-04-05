#TUGAS DASAR PEMROGRAMAN
#PROGRAM TIKET BIOSKOP

#MEMANGGIL MODUL SYS SEBAGAI PROGRAM
import sys as program

#MEMBUAT FUNGSI MAIN SEBAGAI TITIK EKSEKUSI FILE PROGRAM
def main():
    
    #INPUT NAMA LENGKAP
    print("\n")
    nama = input("Masukkan Nama Lengkap     : ")

    #PEMANGGILAN NAMA FILM MENGGUNAKAN FOR LOOP
    print("Daftar film")
    daftar = ["1. Pengabdi Setan", "2. Midsommar", "3. Avengers", "4. Bladerunner", "5. Batman"]
    for i in daftar:
    	print(i)

    #PEMILIHAN JUDUL FILM MENGGUNAKAN PERCABANGAN
    film = input("Pilih judul film (1/2/3/4/5): ")

    if film == "Pengabdi Setan" or film =="pengabdi setan" or film == "1":
        film = "(1) Pengabdi Setan"
        harga = 60000
    elif film == "Midsommar" or film == "midsommar" or film == "2":
        film = "(2) Midsommar"
        harga = 50000
    elif film == "Avengers" or film == "avengers" or film == "3":
        film = "(3) Avengers"
        harga = 30000
    elif film == "Bladerunner" or film == "bladerunner" or film == "4":
        film = "(4) Bladerunner"
        harga = 70000
    elif film == "Batman" or film == "batman" or film == "5":
        film = "(5) Batman"
        harga = 40000
    else:
        print("Judul film yang anda input salah")
        return main()
        #JIKA JUDUL FILM YANG DIINPUT TIDAK SESUAI, MAKA PROGRAM AKAN TERULANG
        
    #INPUT JUMLAH TIKET YANG INGIN DIBELI
    jumlah = int(input("Masukkan Jumlah Tiket       : "))

    #DISKON 10% JIKA PEMBELIAN TOTAL DIATAS 5 TIKET
    if jumlah >= 5:
        potongan = (jumlah * harga) * 0.1
    else:
        potongan = 0
    total = (jumlah * harga) - potongan

    #OUTPUT PROGRAM PENJUALAN TIKET BIOSKOP
    print("\n")
    print("=================================================")
    print("             PENJUALAN TIKET BIOSKOP")
    print("=================================================")
    #MEMANGGIL INPUT NAMA PEMBELI
    print("Nama Pembeli			:", nama)
    #MEMANGGIL INPUT JUDUL FILM YANG DIPILIH
    print("Judul film yang Dipilih		:", film)
    #MENAMPILKAN HARGA PER TIKET
    print("Harga				: Rp.", harga)
    #MENAMPILKAN JUMLAH TIKET YANG DIBELI
    print("Jumlah Tiket			:", jumlah)
    print("=================================================")
    #MENAMPILKAN DISKON YANG DIDAPAT (JIKA TIDAK MEMENUHI SYARAT MAKA DISKON = 0)
    print("Potongan yang Didapat           : Rp.", potongan)
    #MENAMPILKAN JUMLAH TOTAL BAYAR
    print("Total Bayar			: Rp.", total)
    bayar = int(input("Masukkan Uang Bayar		: Rp. "))
    #JIKA UANG PEMBAYARAN LEBIH KECIL DARI TOTAL BAYAR, MAKA PROGRAM BERHENTII
    if bayar < total:
        print("============= Uang tidak mencukupi ==============")
    #JIKA UANG PEMBAYARAN LEBIH BESAR DARI TOTAL BAYAR, MAKA PROGRAM AKAN MENGEMBALIKAN HASIL KEMBALIAN
    else:
        print("Uang Kembali			: Rp.", (bayar - total))
    print("\n")

#PERULANGAN DENGAN MEMANFAATKAN IMPORT 'SYS'
while True:
    #MEMANGGIL FUNGSI MAIN
    main() 
    ulang = input("Ingin beli tiket lagi?(Y/N): ")
    if ulang == 'Y' or ulang == 'y':
        #JIKA PEMBELI INGIN MEMBELI TIKET LAGI, MAKA PROGRAM AKAN DIULANG
        continue
    elif ulang == 'N' or ulang == 'n':
        #JIKA PEMBELI TELAH SELESAI TRANSAKSI, MAKA PROGRAM AKAN BERHENTI
        print("Terima kasih telah membeli tiket kami!")
        program.exit()
    else:
        #JIKA PEMBELI SALAH INPUT, MAKA PROGRAM AKAN BERHENTI
        print("Maaf, input yang anda masukkan salah!")
        program.exit()
