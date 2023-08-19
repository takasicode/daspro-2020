class Solution(object) :
    def Kabisat(self,t,b) :
        tahun = 0
        if t % 4 == 0 :
            tahun = 1
        elif t % 100 == 0 :
            tahun = 0
        elif t % 400 == 0 :
            tahun = 1
        if b == "Februari" or b == "Februari" :
            return 28 + tahun
        angka = ["Januari","Maret","Mei","Juli","Agustus","Oktober","Desember","Januari","Jaret","Mei","Juli","Agustus","Oktober","Desember"]
        if b in angka :
            return 31
        return 30
ob = Solution()

bln = str(input("Masukkan Bulan : "))
thn = int(input("Masukkan Tahun : "))
print("Jumlah Hari Bulan",bln,thn,"=",ob.Kabisat(thn,bln))