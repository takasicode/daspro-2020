def inputMatakuliah(matakuliah) :
    for i in range(len(matakuliah)) :
        matakuliah[i] = input('Mata Kuliah ke-'+str(i+1)+'  : ')

def inputNilaiAngka(nilaiAngka,matakuliah) :
    for i in range(len(nilaiAngka)) :
        nilaiAngka[i] = int(input('Nilai Mata Kuliah '+matakuliah[i]+'   : '))

def nilaiHuruf(nilaiAngka,nilaiHuruf) :
    for i in range(len(nilaiHuruf)) :
        if nilaiAngka[i] <= 100 and nilaiAngka[i] >= 80 :
            nilaiHuruf[i] = 'A'
        elif nilaiAngka[i] < 80 and nilaiAngka[i] >= 70 :
            nilaiHuruf[i] = 'B'
        elif nilaiAngka[i] < 70 and nilaiAngka[i] >= 60 :
            nilaiHuruf[i] = 'C'
        elif nilaiAngka[i] < 60 and nilaiAngka[i] >= 50 :
            nilaiHuruf[i] = 'D'
        elif nilaiAngka[i] < 50 and nilaiAngka[i] >= 0 :
            nilaiHuruf[i] = 'E'
        
def IPK(nilai,nilaiHuruf) :
    for i in range(len(nilai)) :
        if nilaiHuruf[i] == 'A' :
            nilai[i] = 4
        if nilaiHuruf[i] == 'B' :
            nilai[i] = 3
        if nilaiHuruf[i] == 'C' :
            nilai[i] = 2
        if nilaiHuruf[i] == 'D' :
            nilai[i] = 1
        if nilaiHuruf[i] == 'E' :
            nilai[i] = 0

    IPK = sum(nilai)/len(nilai)
    print('IPK  :',IPK)
    if IPK >= 3.5 :
        print('Keterangan   : Cumlaude')
    else :
        print('Keterangan   : Tidak Cumlaude')

def displayTranskrip(nim,nama,matakuliah,nilaiAngka,nilaiHuruf,nilai) :
    print('NIM  : '+str(nim))
    print('Nama : '+str(nama))
    for i in range(len(matakuliah)) :
        print('Mata Kuliah : '+str(matakuliah[i])+'  >>  Nilai Angka :', nilaiAngka[i],'  >>  Nilai Huruf :',nilaiHuruf[i])
    IPK(nilai,nilaiHuruf)