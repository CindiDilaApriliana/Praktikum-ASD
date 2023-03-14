#MODUL 1
#CINDI DILA APRILIANA_L200200106

#NOMOR 7

def faktorPrima(n):
    factor=[]
    a=2
    while a <= n:
        if n % a:
            a+=1
        else:
            n /= a
            factor.append(a)
    return factor
