# kamus
ganjil=[]*5
genap=[]*5

# algoritma
for i in range(10):
    x=int(input("Bilangan :"))
    if x%2==0:
        genap.append(x)
    elif x%2 != 0:
        ganjil.append(x)
total= ganjil + genap
print(total)