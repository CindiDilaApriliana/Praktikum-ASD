#MODUL 6
#CINDI DILA APRILIANA_L200200106

#NOMOR 4
from time import time as detak
from random import shuffle as kocok
import time 
 
def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q] 
    A[q] = tmp 
 
def cariPosisiYangTerkecil(A, dariSini, sampaiSini): 
    posisiYangTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i] < A[posisiYangTerkecil]: 
            posisiYangTerkecil = i 
    return posisiYangTerkecil 
 
def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)
def selectionSort(A): 
    n = len(A)
    for i in range(n - 1): 
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i: 
            swap(A, i, indexKecil) 
             
def insertionSort(A): 
    n = len(A)
    for i in range(1, n): 
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos -1 
        A[pos] = nilai 
         
def mergeSort(A):
    if len(A) > 1: 
        mid = len(A) // 2
        separuhKiri = A[:mid] 
        separuhKanan = A[mid:] 
 
        mergeSort(separuhKiri) 
        mergeSort(separuhKanan) 
 
        i=0; j=0; k=0
        while i < len(separuhKiri) and j < len(separuhKanan): 
            if separuhKiri[i] < separuhKanan[j]:
                A[k] = separuhKiri[i] 
                i = i + 1
            else: 
                A[k] = separuhKanan[j]
                j = j + 1 
            k = k + 1 
 
        while i < len(separuhKiri):
            A[k] = separuhKiri[i] 
            i = i + 1 
            k = k + 1 
 
        while j < len(separuhKanan):
            A[k] = separuhKanan[j]
            j = j + 1 
            k = k + 1 
             
def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1) 
 
def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, titikBelah + 1, akhir) 
        quickSortBantu(A, awal, titikBelah - 1) 
         
def partisi(A, awal, akhir):
    nilaiPivot = A[awal] 
    penandaKiri = awal + 1 
    penandaKanan = akhir 
 
    selesai = False
    while not selesai: 
 
        while penandaKiri <= penandaKanan and A[penandaKiri] <= nilaiPivot: 
            penandaKiri = penandaKiri + 1 
 
        while penandaKanan >= penandaKiri and A[penandaKanan] >= nilaiPivot:
            penandaKanan = penandaKanan - 1 
 
        if penandaKanan < penandaKiri: 
            selesai = True
        else: 
            temp = A[penandaKiri] 
            A[penandaKiri] = A[penandaKanan] 
            A[penandaKanan] = temp 
 
    temp = A[awal] 
    A[awal] = A[penandaKanan] 
    A[penandaKanan] = temp 
 
    return penandaKanan 
             
k = list(range(6000))
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]
u_mrg = k[:]
u_qck = k[:]

aw=detak();bubbleSort(u_bub);ak=detak();print('bubble: %g detik' %(ak-aw)); 
aw=detak();selectionSort(u_bub);ak=detak();print('selection: %g detik' %(ak-aw)); 
aw=detak();insertionSort(u_bub);ak=detak();print('insertion: %g detik' %(ak-aw)); 
aw=detak();mergeSort(u_mrg);ak=detak();print("merge: %g detik" %(ak-aw)); 
aw=detak();quickSort(u_qck);ak=detak();print("quick: %g detik" %(ak-aw)); 
