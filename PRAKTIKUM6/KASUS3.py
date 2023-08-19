#Kamus
sum = 0
i = 1

#Algoritma
n = int(input("Masukan bilangan bulat positif"))
while i <= n:
    print (i)
    sum = sum + 1
    i= i +1
    #i=i : 0=0+1
    #i=2 : 1=1+2
    #i=3 : 3=3+3
print ("Hasil penjumlahan dari 1 sampai "+str(n)+" adalah "+str(sum))