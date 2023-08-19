#Algoritma
tahun=int(input("masuk tahun :"))
if(tahun <2020) :
    selisihTahun=2020-tahun
    print ("Selisih tahun:", selisihTahun)
    selisihBiaya=selisihTahun*2
    print ("Harga Motor Baru 20 juta")
    print ("Motor Anda dihargai", (20-selisihBiaya), "juta")
    print ("Total Pembayaran:")    
else:
    print("sudah motor keluaran terbaru")