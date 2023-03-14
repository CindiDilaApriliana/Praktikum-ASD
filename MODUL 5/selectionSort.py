#CINDI DILA APRILIANA_L200200106
#MODUL 5

#selectionSort

from Latihan1 import *
from Latihan2 import *

def selectionSort(A):
    n = len(A)
    for i in range(n - 1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)
