print('Masukkan 0 untuk mengakhiri')
list = []
while True :
    bilangan = int(input('Masukkan Bilangan = '))
    list.append(bil)
    if bilangan == 0 :
        list.pop()
        break

terkecil=min(list)
terbesar=max(list)
print('\nBilangan Terkecil =', terkecil)
print('Bilangan Terbesar =', terbesar)