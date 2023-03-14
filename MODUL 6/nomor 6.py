#MODUL 6
#CINDI DILA APRILIANA_L200200106

#NOMOR 6

class MhsTIF(object):
    def __init__(self,nama,nim,kota,saku):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.saku = saku
        
        
c0 = MhsTIF('Ika',100,'Sukoharjo', 240000)
c1 = MhsTIF('Budi',101,'Sragen', 230000)
c2 = MhsTIF('Ahmad',103,'Surakarta', 250000)
c3 = MhsTIF('Chandra',104,'Surakarta', 235000)
c4 = MhsTIF('Eka',105,'Boyolali', 240000)
c5 = MhsTIF('Fandi',106,'Salatiga', 250000)
c6 = MhsTIF('Deni',107,'Klaten', 245000)
c7 = MhsTIF('Galuh',108,'Wonogiri', 245000)
c8 = MhsTIF('Janto',109,'Klaten', 245000)
c9 = MhsTIF('Hasan',109,'Karanganyar', 270000)
c10 = MhsTIF('Khalid',110,'Purwodadi', 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def quickSort(A):
    quickSortBantu(A, 0, len(A))

def quickSortBantu(A, awal, akhir):
    hasil = 0
    if awal < akhir:
        titikBelah, hasil = partisi(A, awal, akhir)
        hasil += quickSortBantu(A, titikBelah + 1, akhir)
        hasil += quickSortBantu(A, awal, titikBelah)
    return hasil

def partisi(A, awal, akhir):
    hasil = 0 
    pivot, pidx = mediandaritiga(A, awal, akhir)
    A[awal], A[pidx] = A[pidx], A[awal]
    i = awal + 1
    
    for j in range(awal+1, akhir, 1):
        hasil += 1
        if (A[j] < pivot):
            A[i], A[j] = A[j], A[i]  
            i += 1
    A[awal], A[i-1] = A[i-1], A[awal] 

    return i - 1, hasil

def mediandaritiga(A, awal, akhir):
    tengah = (awal + akhir - 1) // 2
    a = A[awal]
    b = A[tengah]
    c = A[akhir - 1]
    if a <= b <= c:
        return b, tengah
    if c <= b <= a:
        return b, tengah
    if a <= c <= b:
        return c, akhir - 1
    if b <= c <= a:
        return c, akhir - 1
    return a, awal

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
for x in con(inlist, Daftar):
    print("=>", x.nama, x.kota, x.saku, x.nim)
