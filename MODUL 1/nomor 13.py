#MODUL 1
#CINDI DILA APRILIANA_L200200106

#NOMOR 13



def katakan(n):
    ucapan = ['','Satu','Dua','Tiga','Empat','Lima','Enam','Tujuh','Delapan','Sembilan','Sepuluh','Sebelas']
    if n <= 1000000000:
        hasil=''
        if n >= 0 and n <= 11:
            hasil = ucapan[n]
        elif n <20:
            hasil = ucapan[n-10] + ' Belas'
        elif n < 100:
            hasil = katakan(int(n/10)) + " Puluh " + ucapan[n%10]
        elif n < 200:
            hasil = 'Seratus ' + katakan(int(n-100))
        elif n < 1000:
            hasil = katakan(int(n/100)) + ' Ratus '+ katakan(int(n%100))
        elif n < 2000:
            hasil = 'Seribu '+katakan(n-1000)
        elif n < 1000000:
            hasil = katakan(int(n/1000)) + ' Ribu ' + katakan(int(n%1000))
        elif n < 1000000000:
            hasil = katakan(int(n/1000000)) + ' Juta '+ katakan(int(n%1000000))
        elif n == 1000000000:
            hasil = "Satu Milyar"
        return str(hasil)
    else:
        return "Jumlah tidak boleh lebih dari 1 milyar"
