#MODUL 1
#CINDI DILA APRILIANA_L200200106

#NOMOR 6

def bilanganPrima(n):
    for i in range(2,n):
        prima=True
        for j in range(2,i):
            if ( i % j == 0):
                prima = False
        if prima:
            print(i)
