#Algoritma
uangsaku=int(input("masukan uang saku Soni:"))
pengeluaran=1200000
if (uangsaku>pengeluaran) :
    if (uangsaku-pengeluaran>=500000) :
        print("Soni jadi nonton konser dengan tempat duduk biasa")
    elif(uangsaku-pengeluaran>=1000000) :
        print("Soni jadi menonton konser dengan tempat duduk VIP")
    else :
        print("Soni tidak jadi menonton konser karena uang kurang")  
else:
    print("uang saku tidak valid")   