#MODUL 1
#CINDI DILA APRILIANA_L200200106

#NOMOR 14

def formatRupiah(angka):
    hasil = "Rp. {:,.0f}".format(angka).replace(',','.')
    return hasil
