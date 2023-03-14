#CINDI DILA APRILIANA_L200200106
#MODUL 5

#insertionSort

from insertionSort import *

a = [1, 12, 41, 5, 6, 8, 12, 15]
b = [7, 5, 3, 2, 1, 13, 67]
        
def urutAB(a, b):
    c = a + b
    insertionSort(c)
    return c

print(urutAB(a,b))
