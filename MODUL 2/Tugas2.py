#MODUL 2
#CINDI DILA APRILIANA_L200200106


"""untuk no 2, 3, 4, 5, 6, 7 tetap menggunakan kode ini"""

class Manusia(object):
    def __init__(self,nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('Salam, namaku',self.nama)
    def makan(self,s):
        print('Saya baru saja makan',s)
        self.keadaan = 'kenyang'
    def olahraga(self,k):
        print('Saya baru saja Latihan',k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self,n):
        return n*2
    
class Mahasiswa(Manusia):
    
    def __init__(self,nama,nim,kota,us):
        self.nama = nama
        self.Nim = nim
        self.kotaTinggal = kota
        self.uangSaku = us
        self.MK = []
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.Nim) \
        + '. Tinggal di ' + self.kotaTinggal \
        + '. Uang saku Rp ' + str(self.uangSaku) \
        + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.Nim
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self,x):
        self.kotaTinggal = x
    def ambilUangSaku(self):
        return self.uangSaku
    def tambahUangSaku(self,y):
        self.uangSaku += int(y)
    def makan(self,s):
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan = 'kenyang'
    def listKuliah(self):
        return self.MK
    def ambilKuliah(self,x):
        self.MK.append(x)
    def hapusMK(self,x):
        self.MK.remove(x)
m9 = Mahasiswa('Cindi', 676,'Ngawi',500000)

#NOMOR 2
print(m9.ambilKotaTinggal())
m9.perbaruiKotaTinggal('palembang')
print(m9.ambilKotaTinggal())
print(m9.ambilUangSaku())
m9.tambahUangSaku(50000)
print(m9.ambilUangSaku())



