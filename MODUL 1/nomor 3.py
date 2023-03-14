#MODUL 1
#CINDI DILA APRILIANA_L200200106

#NOMOR 3

#NOMOR 3A

def jumlahHurufVokal(hrf):
    vokal="aiueoAIUEO"
    a = 0
    hasil = 0
    for i in hrf:
        if i in vokal:
            a += len(i)
        else:
                a +=0
    hasil = len (hrf),a
    return hasil


#NOMOR 3B

def jumlahHurufKonsonan(hrf):
    konsonan="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    b = 0
    hasil = 0
    for i in hrf:
        if i in konsonan:
            b += len(i)
        else:
                b +=0
    hasil = len (hrf),b
    return hasil
