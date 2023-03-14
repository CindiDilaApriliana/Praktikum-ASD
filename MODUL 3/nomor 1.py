#MODUL 3
#CINDI DILA APRILIANA_L200200106

#Nomor 1
a = [[4,5],[3,6]]
b = [[3,2],[3,5]]
c = [[4,1],[3,5],[6,5,2]]


def cekMatriks(x):
    for i in x:
        if len(i) != len(x):
            return "isi dan ukuran matriks tidak konsisten"
            break
        else :
            return "isi dan ukuran matriks konsisten"

#untuk mengambil ukuran matrixnya
def mengambilUkuran(x):
    hasil = len(x), len(x[0])
    return hasil


# untuk menjumlahkan dua matrix (pastikan ukurannya sesuai)
def hitungArray(x,y):
    hasil = []
    for i in range(len(x)):
        baru =[]
        for n in range(len(x[i])):
            baru.append(x[i][n]+y[i][n])
        hasil.append(baru)
    return hasil    
                        
#untuk mengalikan dua matrix (pastikan ukurannya sesuai)
def kaliArray(x,y):
    hasil = []
    for i in range(len(x)):
        baru =[]
        for n in range(len(x[i])):
            baru.append(x[i][n]*y[i][n])
        hasil.append(baru)
    return hasil

#untuk menghitung determinan sebuah matrix bujursangkar
def detMatriks(x):
    for i in range(len(x)):
        if i ==0:
            ad = x[i][i]*x[i+1][i+1]
        elif i == 1:
            bc = x[i-1][i]*x[i][i-1]
    hasil = ad - bc
    return hasil
