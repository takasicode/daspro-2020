import random

##Kamus
saldo = int(input("masukkan saldo awal : "))
tanggalLahirSMS = int(input("Kapan tanggal lahir mama : "))
tanggalLahirMama = 12
jumlahDikirim = int(input("Masukkan jumlahpulsa yang diinginkan mama :"))
counter = 0.0
randCounter = random.randint(0,9)

#Algoritma
if tanggalLahirSMS != tanggalLahirMama:
    print("Ini penipu!")

elif jumlahDikirim > saldo :
    print("saldo tidak cukup")

else :
    for i in range(randCounter):
        while counter <= 0.5:
            counter = random.random()
            print("silakan tunggu...")
        if i == 2:
            print("transaksi gagal")
            break
    print("transaksi berhasil")
