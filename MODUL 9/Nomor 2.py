#MODUL 9
#CINDI DILA APRILIANA_L200200106

class _SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

A = _SimpulPohonBiner('Ambarawa')
B = _SimpulPohonBiner('Bantul')
C = _SimpulPohonBiner('Cimahi')
D = _SimpulPohonBiner('Denpasar')
E = _SimpulPohonBiner('Enrekang')
F = _SimpulPohonBiner('Flores')
G = _SimpulPohonBiner('Garut')
H = _SimpulPohonBiner('Halmahera Timur')
I = _SimpulPohonBiner('Indramayu')
J = _SimpulPohonBiner('Jakarta')

A.kiri = B; A.kanan = C
B.kiri = D; B.kanan = E
C.kiri = F; B.kanan = G
E.kiri = H
G.kanan = I

#No 2
def tinggiPohon(akar):
    if akar is None:
        return 0
    else :
        dalamkiri = tinggiPohon(akar.kiri)
        dalamkanan = tinggiPohon(akar.kanan)

        if(dalamkiri > dalamkanan):
            return dalamkiri + 1
        else :
            return dalamkanan + 1

print('Tinggi pohon A : ', tinggiPohon(A))
