def hapusKuliah(self,Makul):
    if Makul in self.listKuliah:
        self.listKuliah.remove(Makul)
        print("Berhasil Menghapus Kuliah",Makul,"dari List")
        else :
        print("Mata Kuliah",Makul,"belum diambil")


m9 = Mahasiswa('Jarot',247,'Colomadu',200000)
print(m9.ambilKotaTinggal())
print('')
m9.perbaruiKotaTinggal('Surakarta')
print(m9.ambilKotaTinggal())
print('')
print(m9.ambilUangSaku())
m9.tambahUangSaku(200000)
print(m9.ambilUangSaku())
