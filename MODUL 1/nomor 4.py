#MODUL 1
#CINDI DILA APRILIANA_L200200106

#NOMOR 4

def rerata(b):
    jumlah = 0 
    for i in range (len(b)):
        jumlah += b[i]
    jumlah = jumlah/len(b)
    return jumlah
