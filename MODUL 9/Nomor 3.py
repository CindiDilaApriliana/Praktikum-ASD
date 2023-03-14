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

# no 3
d = [A.data, B.data, C.data, D.data, E.data, H.data, I.data, J.data]
def traverse(akar):
    levellist=[]
    arlvl = [akar]
    lvl = 0
    while arlvl:
        nextlvl = list()
        for a in arlvl:
            if a.kiri:
                nextlvl.append(a.kiri)
                level.append(lvl+1)
            if a.kanan:
                nextlvl.append(a.kanan)
                level.append(lvl+1)
            arlvl = nextlvl        
        lvl += 1
        levellist.append(lvl)
    return levellist
def cetak(akar):
    traverse(A)
    print(akar.data, ', Level 0')
    for i in range(len(level)):
          print(d[i+1], ', Level', level[i])
level = []
cetak(A)
