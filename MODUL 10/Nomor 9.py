#MODUL 10
#CINDI DILA APRILIANA_L200200106

#NOMOR 9
import timeit
import time
import matplotlib.pyplot as plt

def straight(cont, target):
    n = len(cont)
    for i in range(n):
        if cont[i] == target:
            return True
    return False

def tim():
    a = 100
    b = [12, 3, 5, 6, 8, 2, 11]
    awal = time.time()
    U = straight(b, a)
    akhir = time.time()
    print('Worst case')
    print('mengurutkan %d bilangan, memerlukan %8.7f detik' % (U, akhir-awal))

tim()

def kalangBersusuh(n):
    a = 100
    b = [12, 3, 5, 6, 8, 2, 11]
    U = straight(b, n)

def ujiKalangBersusuh(n):
    ls = []
    jangkauan =  range(1, n+1)
    siap = 'from __main__ import kalangBersusuh'
    for i in jangkauan:
        print('i = ', i)
        t = timeit.timeit('kalangBersusuh(' + str(i) +')', setup = siap, number = 1)
        ls.append(t)
    return ls

n = 100
LS = ujiKalangBersusuh(n)
plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1, n+1)])
plt.show()
