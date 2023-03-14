#MODUL 7
#CINDI DILA APRILIANA_L200200106

#NOMOR 4

import re

f = open ("KEI.html","r",encoding='latin1')
s = f.read()
f.close()
pola = r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>'
cocok = re.findall(pola, s)
baru = []
for i in cocok:
    a = (i[0], float(i[4]))
    baru.append(a)
print(baru)
