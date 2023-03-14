#MODUL 10
#CINDI DILA APRILIANA_L200200106

#nomor 2
from timeit import timeit
import random

print("------average case scenario------")        
for i in range(5):
    g = list(range(3000))
    random.shuffle(g)
    t = timeit('sorted(g)', setup =  'from __main__ import g', number=1)
    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(g), t))
    
print("------worst case scenario------") 
for i in range(5):
    g = list(range(3000))
    g = g[::-1]
    t = timeit('sorted(g)', setup =  'from __main__ import g', number=1)
    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(g), t))
    
print("------best case scenario------") 
for i in range(5):
    g = list(range(3000))
    t = timeit('sorted(g)', setup =  'from __main__ import g', number=1)
    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(g), t))
