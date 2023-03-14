class siswaSMA(Manusia):
    def __init__(self,nama):
        self.nama = nama
        self.noAbsen = ''
        self.kelas = ''
    def editNama(self,nama):
        self.nama = nama
    def insertAbsen(self,x):
        self.noAbsen = int(x)
    def insertKelas(self,x):
        self.kelas = x
    def tampilID(self):
        return self.nama,self.noAbsen,self.kelas

s1 = siswaSMA('Andika')
s1.editNama('Andika Risky Faizatama')
s1.insertAbsen('3')
s1.insertKelas('12 MIPA 1')
print(s1.tampilID())
