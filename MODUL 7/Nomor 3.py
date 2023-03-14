#MODUL 7
#CINDI DILA APRILIANA_L200200106

#NOMOR 3

import re

f = open ("Indonesia.txt", "r")
s = f.read()
f.close()
pola = r'di\s\w+'
tampilkan = re.findall(pola,s)
print(tampilkan)
