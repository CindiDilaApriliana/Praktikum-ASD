#CINDI DILA APRILIANA_L200200106
#MODUL 5

#bubbleSort

from Latihan1 import*
def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                 swap(A,j,j+1)
