#Kamus
bilangan = 0

#Algoritma
bilangan = int(input("Masukan bilangan"))
if bilangan > 1:
    for i in range(2,bilangan):
        if (bilangan % i) == 0:
            print("Bukan bilangan prima")
            break
else:
    print("Bilangan prima")