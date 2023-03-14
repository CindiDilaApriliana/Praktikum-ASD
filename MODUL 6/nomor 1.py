#MODUL 6
#CINDI DILA APRILIANA_L200200106

#NOMOR 1

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

def mengeSort(A):
    if len (A)>1:
        mid = len(A)//2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]

        mengeSort(separuhKiri)
        mengeSort(separuhKanan)

        i=0;j=0;k=0
        while i <len(separuhKiri)and j < len(separuhKanan):
            if separuhKiri[i]<separuhKanan[j]:
                A[k]=separuhKiri[i]
                i=i+1
            else:
                A[k]=separuhKanan[j]
                j=j+1
            k=k+1

        while  i <len(separuhKiri):
            A[k]=separuhKiri[i]
            i=i+1
            k=k+1

        while j<len(separuhKanan):
            A[k]=separuhKanan[j]
            j=j+1
            k=k+1

def con(a,b):
    baru=[]
    for x in range (len (a)):
       for y in range (len (a)):
           if a [x]==b[y].nama:
               baru.append(b[y])
    return baru

inlist  =[]
for x in Daftar:
    inlist.append(x.nama)

print('Pengaturan Berdasarkan Nama')
mengeSort(inlist)
for x in con(inlist,Daftar):
    print("=>",x.nama, x.kota, x.saku, x.nim)
