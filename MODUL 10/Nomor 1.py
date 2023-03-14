#MODUL 10
#CINDI DILA APRILIANA_L200200106


#NOMOR 1A
import time
from timeit import timeit

def jumlahkan_cara_1(n):
    hasilnya = 0
    for i in range(1, n+1):
        hasilnya = hasilnya + i
    return hasilnya

for i in range(5):
    siap = 'from __main__ import jumlahkan_cara_1'
    h = jumlahkan_cara_1(1000000)
    t = timeit('jumlahkan_cara_1(1000000)', setup =  siap, number=1)
    print("Jumlah adalah %d, memerlukan %9.8f detik" % (h, t))



NOMOR 1B

import time
from timeit import timeit

def jumlahkan_cara_2(n):
    return (n*(n + 1))/2

for i in range(5):
    siap = 'from __main__ import jumlahkan_cara_2'
    h = jumlahkan_cara_2(1000000)
    t = timeit('jumlahkan_cara_2(1000000)', setup =  siap, number=1)
    print("Jumlah adalah %d, memerlukan %9.8f detik" % (h, t))

NOMOR 1C
import random
from timeit import timeit

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos -1
        A[pos] = nilai

print("------average case scenario------")        
for i in range(5):
    siap = 'from __main__ import insertionSort, L'
    L = list(range(3000))
    random.shuffle(L)
    t = timeit('insertionSort(L)', setup =  siap, number=1)
    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L), t))
    
print("------worst case scenario------") 
for i in range(5):
    siap = 'from __main__ import insertionSort, L'
    L = list(range(3000))
    L = L[::-1]
    t = timeit('insertionSort(L)', setup =  siap, number=1)
    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L), t))
    
print("------best case scenario------") 
for i in range(5):
    siap = 'from __main__ import insertionSort, L'
    L = list(range(3000))
    t = timeit('insertionSort(L)', setup =  siap, number=1)
    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L), t))
