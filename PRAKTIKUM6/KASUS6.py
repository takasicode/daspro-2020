#Algoritma
sisaSaldo = saldoAwal
pengeluaran = 0
saldoAwal = int(input("Masukan saldo awal:"))
while (pengeluaran!= -1) :
    pengeluaran=int(input("Masukan pengeluaran :"))
    if((pengeluaran>0)and ((sisaSaldo-pengeluaran)>0)) :
        sisaSaldo=sisaSaldo-pengeluaran ;
    else:
        if  (pengeluaran!= -1) :
            print ("sisa saldo tidak cukup, ", end="")
        break
print("sisa saldo" ,sisaSaldo)