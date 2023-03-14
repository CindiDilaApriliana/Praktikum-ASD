#MODUL 4
#CINDI DILA APRILIANA_L200200106

class MhsTIF(object):
    def __init__(self,nama,umur,kota,saku):
        self.nama = nama
        self.umur = umur
        self.kota = kota
        self.saku = saku
        
        
c0 = MhsTIF('Ika',10,'Sukoharjo', 240000)
c1 = MhsTIF('Budi',51,'Sragen', 230000)
c2 = MhsTIF('Ahmad',2,'Surakarta', 250000)
c3 = MhsTIF('Chanra',18,'Surakarta', 235000)
c4 = MhsTIF('Eka',4,'Boyolali', 240000)
c5 = MhsTIF('Fandi',31,'Salatiga', 250000)
c6 = MhsTIF('Deni',13,'Klaten', 245000)
c7 = MhsTIF('Galuh',5,'Wonogiri', 245000)
c8 = MhsTIF('Janto',23,'Klaten', 245000)
c9 = MhsTIF('Hasan',64,'Karanganyar', 270000)
c10 = MhsTIF('Khalid',29,'Purwodadi', 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
##
###nomor 1
##
##def mencari(data,cari):
##    x = []
##    for i in range(len(data)):
##        if (data[i].kota == cari):
##            x.append(i)
##    if len(x)>0:
##        print(x)
##        return True
##    else:
##        print(x)
##        return False
##    
##
##print(mencari(Daftar,'Klaten'))

###Nomor 2
##def uangTerkecil(kumpulan):
##    terkecil = kumpulan[0]
##    for i in kumpulan:
##        if i.saku < terkecil.saku:
##            terkecil = i
##    print(terkecil.nama ,'memiliki uang saku paling sedikit yaitu ',terkecil.saku)
##uangTerkecil(Daftar)


#Nomor 3
##def listuangTerkecil(kumpulan):
##    ls = []
##    terkecil = kumpulan[0]
##    for i in kumpulan:
##        if i.saku < terkecil.saku:
##            terkecil = i
##        elif i.saku > terkecil.saku:
##            continue
##        elif i.saku == terkecil.saku:
##            ls.append(i)
##        return ls
##X = listuangTerkecil(Daftar)
##for i in X:
##    print(i.nama)
##
###Nomor 4
##def kurang250000(kumpulan):
##    ls = []
##    for i in kumpulan:
##        if i.saku < 250000:
##            ls.append(i)
##        else:
##            continue
##        return ls
##Z = kurang250000(Daftar)
##for i in Z:
##    print(i.nama,i.saku)


#Nomor 5

class Node():
    def __init__(self, data, link=None):
        self.data = data
        self.next = link
        
    def cariItem(self, cari):
        x = self
        awal = 1
        while x != None:
            if x.data == cari:
                return "Item berada di simpul ke - " + str(awal)
            else:
                awal += 1
                x = x.next
        return "Item tidak ditemukan"
 
a = Node(10)
a.next = Node(15)
a.next.next = Node(20)


#Nomor 6
kumpulan=[2,4,6,8,10,12,14,16,18,20]
def binSe(kumpulan,target):
    low = 0
    high = len(kumpulan)-1
    
    while low <=high:
        mid =(high + low)//2
        if kumpulan[mid]==target: 
            return 'ditemukan pada indeks ke-'+str(mid)
        elif target < kumpulan[mid]:
            high = mid -1
        else:
            low = mid+1
    return False

#Nomor 7
data = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]

def binSe2(kumpulan,target):
    low = 0
    high = len(kumpulan)-1
    ketemu = False
    x = []
    while low <= high and not ketemu :
        mid = (high + low)//2
        if kumpulan[mid] == target:
            ketemu = True
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
    if not ketemu:
        print('Data tidak ditemukan')
    for i in range(len(kumpulan)):
        if kumpulan[i] == target:
            x.append(mid)
            mid+=1
    return x

