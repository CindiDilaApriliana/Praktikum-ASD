#MODUL 1
#CINDI DILA APRILIANA_L200200106

#NOMOR 10

from math import sqrt as akar
def selesaikanABC(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    if a < 0 :
        print("Determinannya negatif. Persamaan tidak mempunyai akar real")
    elif b < 0:
        print("Determinannya negatif. Persamaan tidak mempunyai akar real")
    elif c < 0:
        print("Determinannya negatif. Persamaan tidak mempunyai akar real")
    else :
        D = b**2 - 4*a*c
        x1 = (-b + akar (D))/(2*a)
        x2 = (-b - akar (D))/(2*a)
        hasil = (x1,x2)
        return hasil
