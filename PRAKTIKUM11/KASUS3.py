print("inputan berupa tahun main Semarang Chester, tahun yang valid 1990 sampai 2020")
print("inputan bisa langsung banyak dengan dipisah tanda spasi, contoh: 1999 2020")
L = list(map(int,input("masukan tahun :").split(" ")))
tahunMenang=[]
jumlahMenang=0
for i in L:
    if i >=1990 and i <=2020:
        if i%2==1: #tahun ganjil
            jumlahMenang+=1
            tahunMenang.append(i)
    else:
        print("tahun", i, "tidak valid")

if len(tahunMenang)>0:
    tahunMenang=sorted(tahunMenang)
    print("Tahun kemenangan Semarang Chaster")
    for i in tahunMenang:
        print(i)
print("Jumlah menang Semarang Chester dari tahun-tahun diatas =", jumlahMenang)