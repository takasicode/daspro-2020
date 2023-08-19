def cekLulus(nilaiHuruf,Keterangan) :
    if len(nilaiHuruf) >= 5 :
        for i in range(len(nilaiHuruf)):
            if nilaiHuruf[i] >= 'E' :
                Keterangan = False
                break
    else:
        Keterangan = False

    if Keterangan == True :
        print('Lulus')
    else :
        print('Tidak Lulus')