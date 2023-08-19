import MyLib as f

def main():
    #input
    nim = input('NIM   : ')
    nama = input('Nama     : ')
    while True:
        jumlahMatakuliah = int(input('Jumlah Mata Kuliah (min 3) : '))
        if jumlahMatakuliah >= 3 :
            break
        else:
            print('minimal 3')
    matakuliah = [str] * jumlahMatakuliah
    nilaiAngka = [int]*jumlahMatakuliah
    nilaiHuruf = [str] * jumlahMatakuliah
    nilai = [float] * jumlahMatakuliah

    f.inputMatakuliah(matakuliah)
    f.inputNilaiAngka(nilaiAngka,matakuliah)
    f.nilaiHuruf(nilaiAngka,nilaiHuruf)
    print('\t')

    f.displayTranskrip(nim,nama,matakuliah,nilaiAngka,nilaiHuruf,nilai)

main()