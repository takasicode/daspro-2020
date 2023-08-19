import MyLib

def main():
    #input
    angka1 = int(input("Masukkan angka pertama untuk aritmatika:"))
    angka2 = int(input("Masukkan angka kedua untuk aritmatika:"))
    s = float(input("Masukkan sisi persegi (float):"))
    a,t = map(float,input("Masukkan a & t segitiga (float)(float):").split())

    #output
    print("Hasil Penjumlahan:", MyLib.Tambah(angka1,angka2))
    print("Hasil Pengurangan:", MyLib.Kurang(angka1,angka2))
    #contoh men-assign hasil fungsi ke variable
    hasilkali = MyLib.Kali(angka1,angka2)
    print("Hasil Perkalian:", hasilkali)
    print("Hasil Pembagian:", MyLib.Bagi(angka1,angka2))
    print("Luas Persegi:", MyLib.LuasPersegi(s))
    print("Luas Segitiga:", MyLib.LuaSegitiga(a,t))

#panggil main program disini
main() 