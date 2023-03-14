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

# no 1
def ukuranPohon(akar):
    if akar is None:
        return 0
    else:
        return (ukuranPohon(akar.kiri) + 1 + ukuranPohon(akar.kanan))

print('Ukuran pohon A : ', ukuranPohon(A))
