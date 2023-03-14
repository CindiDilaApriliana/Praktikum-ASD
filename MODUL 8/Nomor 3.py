#MODUL 8
#CINDI DILA APRILIANA_L200200106

#Nomor 3

from Latihan1 import *

nilai = Stack()
for i in range(16):
    if i%3==0:
        nilai.push(i)
    elif i%4==0:
        nilai.pop()
print(nilai.items)
