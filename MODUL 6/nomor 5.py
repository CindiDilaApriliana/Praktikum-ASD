#MODUL 6
#CINDI DILA APRILIANA_L200200106

#NOMOR 5

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

def mergeSortEf(A, awal, akhir):
    mid = (awal + akhir) // 2
    if awal < akhir:
        mergeSortEf(A, awal, mid)
        mergeSortEf(A, mid + 1, akhir)

    i, j, k = 0, awal, mid + 1
    tmp = [None] * (akhir - awal + 1)
    while j <= mid and k <= akhir:
        if A[j] < A[k]:
            tmp[i] = A[j]
            j += 1
        else:
            tmp[i] = A[k]
            k += 1
        i += 1

    if j <= mid:
        tmp[i:] = A[j:mid + 1]

    if k <= akhir:
        tmp[i:] = A[k:akhir + 1]

    i = 0
    while awal <= akhir:
        A[awal] = tmp[i]
        awal += 1
        i += 1
        
def mergeSort(A):
    mergeSortEf(A, 0, len(A)-1)

def con(a, b):
    baru = []
    for x in range(len(a)):
        for y in range(len(a)):
            if a[x] == b[y].nama:
                baru.append(b[y])
    return baru

ls = []
for x in Daftar:
    ls.append(x.nama)

print('Pengurutan berdasarkan nama')
mergeSort(ls)
for x in con(ls, Daftar):
    print("=>", x.nama, x.kota, x.saku, x.nim)
