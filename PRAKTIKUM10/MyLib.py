def panjangString(s): 
    counter=0
    for char in s:
        counter=counter+1
    return counter

def cariKarakter(c,s):
    ketemu=False
    for i in s:
        if c==i:
            print("ada")
            ketemu=True
            break

    if ketemu==False:
        print("tidak ada")

def frekuensiKarakter(c,s):
    counter=0
    for i in s:
        if c==i:
            counter=counter+1
    return counter

def cekPalindrom(s):
    return s==s[::-1]