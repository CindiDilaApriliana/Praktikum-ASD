#MODUL 2
#CINDI DILA APRILIANA_L200200106


#NOMOR 1

class Pesan (object):
    
    def __init__(self,sebuahString):
        self.teks =  sebuahString
    def cetakIn(self):
        print(self.teks)
    def cetakHurufBesar(self):
        print(str.upper(self.teks))
    def cetakHurufKecil(self):
        print(str.lower(self.teks))
    def jumlah(self):
        return len(self.teks)
    def cetakJumlahKarakter(self):
        print("Kalimat mempunyai", len(self.teks), "Karakterku")
    def perbarui(self, StringNew):
        self.teks = StringNew
    def apakahTerkandung(self, kata):
        if str(kata) in self.teks:
            return True
        else :
            return False

    #NOMOR 1B
    def hitungKonsonan(self):
        vokal="aiueo"
        hasil = 0
        for i in self.teks:
            if i not in vokal and i!='':
                hasil +=1
        return hasil
    
    #NOMOR 1C
    def hitungVokal(self):
        vokal="aiueo"
        hasil = 0
        for i in self.teks:
            if i in vokal:
                hasil +=1
        return hasil
