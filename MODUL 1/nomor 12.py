#MODUL 1
#CINDI DILA APRILIANA_L200200106

#NOMOR 12

from random import randint

bilrandom = randint(1,100)
tebak = 1
print("Program tebak angka")
print("Saya menyimpan sebuah angka bulat antara 1 sampai 100,coba tebak")
print("Tebakan ke-",tebak)
print(bilrandom)
inpt = int(input("Coba Tebak : "))

while(inpt>bilrandom or inpt<bilrandom):
    if(inpt>bilrandom):
        print("Tebakan ke-",tebak,"Terlalu Besar")
        inpt=int(input("Coba tebak Lagi : "))
        tebak+=1
    elif(inpt<bilrandom):
        print("Tebakan ke-",tebak,"Terlalu Kecil")
        inpt=int(input("Coba tebak Lagi : "))
        tebak+=1
print("Ya. Anda benar pada tebakan ke",tebak)
