#MODUL 7
#CINDI DILA APRILIANA_L200200106

#NOMOR 2

import re

f = open ("Indonesia.txt", "r")
s = f.read()
f.close()
pola = r'di\w+'
tampilkan = re.findall(pola,s)
print(tampilkan)
