#MODUL 8
#CINDI DILA APRILIANA_L200200106

#Nomor 1

from Latihan1 import Stack

def cetakHexa(bil):
    x = Stack()
    if bil == 0: x.push(0);
    while bil != 0:
        if bil%16 == 10:
            sisa = "A"
        elif bil%16 == 11:
            sisa = "B"
        elif bil%16 == 12:
            sisa = "C"
        elif bil%16 == 13:
            sisa = "D"
        elif bil%16 == 14:
            sisa = "E"
        elif bil%16 == 15:
            sisa = "F"
        else:
            sisa = bil%16
        bil=bil//16
        x.push(sisa)
    string = ""
    for i in range (len(x)):
        string = string + str(x.pop())
    return string  

