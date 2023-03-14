#MODUL 6
#CINDI DILA APRILIANA_L200200106

#NOMOR 7

from time import time as detak
from random import shuffle as kocok
import time

#Lama
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

#Baru
def mergeSortEf(A, awal, akhir):
    mid = (awal + akhir) // 2
    if awal < akhir:
        mergeSortEf(A, awal, mid)
        mergeSortEf(A, mid + 1, akhir)

    i, j, k = 0, awal, mid + 1
    tmp = [None] * (akhir - awal + 1)
    while j <= mid and k <= akhir:
        if A[j] < A[k]:
            tmp[i] = A[j]
            j += 1
        else:
            tmp[i] = A[k]
            k += 1
        i += 1

    if j <= mid:
        tmp[i:] = A[j:mid + 1]
    if k <= akhir:
        tmp[i:] = A[k:akhir + 1]
    i = 0
    while awal <= akhir:
        A[awal] = tmp[i]
        awal += 1
        i += 1
        
def mergeSortBaru(A):
    mergeSortEf(A, 0, len(A)-1)
    
def quickSortBaru(A):
    quickSortBantuEf(A, 0, len(A))

def quickSortBantuEf(A, awal, akhir):
    hasil = 0
    if awal < akhir:
        titikBelah, hasil = partisiEf(A, awal, akhir)
        hasil += quickSortBantuEf(A, titikBelah + 1, akhir)
        hasil += quickSortBantuEf(A, awal, titikBelah)
    return hasil

def partisiEf(A, awal, akhir):
    hasil = 0 
    pivot, pidx = mediandaritiga(A, awal, akhir)
    A[awal], A[pidx] = A[pidx], A[awal]
    i = awal + 1
    for j in range(awal+1, akhir, 1):
        hasil += 1
        if (A[j] < pivot):
            A[i], A[j] = A[j], A[i]  
            i += 1
    A[awal], A[i-1] = A[i-1], A[awal] 
    return i - 1, hasil

def mediandaritiga(A, awal, akhir):
    tengah = (awal + akhir - 1) // 2
    a = A[awal]
    b = A[tengah]
    c = A[akhir - 1]
    if a <= b <= c:
        return b, tengah
    if c <= b <= a:
        return b, tengah
    if a <= c <= b:
        return c, akhir - 1
    if b <= c <= a:
        return c, akhir - 1
    return a, awal

k =  list(range(6000))
kocok(k)
u_mrg = k[:]
u_qck = k[:]
u_mrgBaru = k[:]
u_qckBaru = k[:]

aw=detak();mergeSort(u_mrg);ak=detak();print("merge: %g detik" %(ak-aw));
aw=detak();quickSort(u_qck);ak=detak();print("quick: %g detik" %(ak-aw));
aw=detak();mergeSortBaru(u_mrgBaru);ak=detak();print("merge baru: %g detik" %(ak-aw));
aw=detak();quickSortBaru(u_qckBaru);ak=detak();print("quick baru: %g detik" %(ak-aw));
