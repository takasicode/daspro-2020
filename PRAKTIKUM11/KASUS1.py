L=[]
i=1
while True:
    el=int(input("masukkan elemen list ke-"+str((i))+":"))
    if el==0:
        break
    else:
        L.append(el)
    i+=1

print(L)