#MODUL 6
#CINDI DILA APRILIANA_L200200106

#NOMOR 2

class MhsTIF(object):
    def __init__(self,nama,nim,kota,saku):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.saku = saku
        
        
c0 = MhsTIF('Ika',100,'Sukoharjo', 240000)
c1 = MhsTIF('Budi',101,'Sragen', 230000)
c2 = MhsTIF('Ahmad',103,'Surakarta', 250000)
c3 = MhsTIF('Chanra',104,'Surakarta', 235000)
c4 = MhsTIF('Eka',105,'Boyolali', 240000)
c5 = MhsTIF('Fandi',106,'Salatiga', 250000)
c6 = MhsTIF('Deni',107,'Klaten', 245000)
c7 = MhsTIF('Galuh',108,'Wonogiri', 245000)
c8 = MhsTIF('Janto',109,'Klaten', 245000)
c9 = MhsTIF('Hasan',109,'Karanganyar', 270000)
c10 = MhsTIF('Khalid',110,'Purwodadi', 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]


def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1)

def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, titikBelah + 1, akhir)
        quickSortBantu(A, awal, titikBelah - 1)
        
def partisi(A, awal, akhir):
    nilaiPivot = A[awal]

    penandaKiri = awal + 1
    penandaKanan = akhir

    selesai = False
    while not selesai:

        while penandaKiri <= penandaKanan and A[penandaKiri] <= nilaiPivot:
            penandaKiri = penandaKiri + 1

        while penandaKanan >= penandaKiri and A[penandaKanan] >= nilaiPivot:
            penandaKanan = penandaKanan - 1

        if penandaKanan < penandaKiri:
            selesai = True
        else:
            temp = A[penandaKiri]
            A[penandaKiri] = A[penandaKanan]
            A[penandaKanan] = temp

    temp = A[awal]
    A[awal] = A[penandaKanan]
    A[penandaKanan] = temp

    return penandaKanan

def con(a, b):
    baru = []
    for x in range(len(a)):
        for y in range(len(a)):
            if a[x] == b[y].nama:
                baru.append(b[y])
    return baru

inlist = []
for x in Daftar:
    inlist.append(x.nama)
    
print('Pengurutan berdasarkan nama')
quickSort(inlist)
for x in con(ls, Daftar):
    print("=>", x.nama, x.kota, x.saku, x.nim)
