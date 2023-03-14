#MODUL 2
#CINDI DILA APRILIANA_L200200106

#NOMOR 3
    
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

m9 = Mahasiswa('Sri', 676,'Yogyakarta',240000)
