#MODUL 10
#CINDI DILA APRILIANA_L200200106

#NOMOR 3A
import timeit
import matplotlib.pyplot as plt

def kalangBersusuh(n):
    test = 0
    for i in range(n):
        for j in range(n):
            test = test + i * j

def ujiKalangBersusuh(n):
    ls = []
    jangkauan =  range(1, n+1)
    siap = 'from __main__ import kalangBersusuh'
    for i in jangkauan:
        print('i = ', i)
        t = timeit.timeit('kalangBersusuh(' + str(i) +')', setup = siap, number = 1)
        ls.append(t)
    return ls

n = 5
LS = ujiKalangBersusuh(n)
plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1, n+1)])
plt.show()


###NOMOR 3B
##import timeit
##import matplotlib.pyplot as plt
##
##def kalangBersusuh(n):
##    test = 0
##    for i in range(n):
##        for j in range(i):
##            test = test + i * j
##
##def ujiKalangBersusuh(n):
##    ls = []
##    jangkauan =  range(1, n+1)
##    siap = 'from __main__ import kalangBersusuh'
##    for i in jangkauan:
##        print('i = ', i)
##        t = timeit.timeit('kalangBersusuh(' + str(i) +')', setup = siap, number = 1)
##        ls.append(t)
##    return ls
##
##n = 1000
##LS = ujiKalangBersusuh(n)
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()
##
###NOMOR 3C
##import timeit
##import matplotlib.pyplot as plt
##
##def kalangBersusuh(n):
##    test = 0
##    for i in range(n):
##        test = test + 1
##    for j in range(n):
##        test = test - 1
##
##def ujiKalangBersusuh(n):
##    ls = []
##    jangkauan =  range(1, n+1)
##    siap = 'from __main__ import kalangBersusuh'
##    for i in jangkauan:
##        print('i = ', i)
##        t = timeit.timeit('kalangBersusuh(' + str(i) +')', setup = siap, number = 1)
##        ls.append(t)
##    return ls
##
##n = 1000
##LS = ujiKalangBersusuh(n)
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()
##
##
###NOMOR 3D
##import timeit
##import matplotlib.pyplot as plt
##
##def kalangBersusuh(n):
##    i = n
##    while i > 0:
##        k = 2 + 2
##        i = i // 2
##
##def ujiKalangBersusuh(n):
##    ls = []
##    jangkauan =  range(1, n+1)
##    siap = 'from __main__ import kalangBersusuh'
##    for i in jangkauan:
##        print('i = ', i)
##        t = timeit.timeit('kalangBersusuh(' + str(i) +')', setup = siap, number = 1)
##        ls.append(t)
##    return ls
##
##n = 1000
##LS = ujiKalangBersusuh(n)
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()
##
##
###NOMOR 3E
##import timeit
##import matplotlib.pyplot as plt
##
##def kalangBersusuh(n):
##    for i in range(n):
##        for j in range(n):
##            for k in range(n):
##                m = i + j + k + 2019
##
##def ujiKalangBersusuh(n):
##    ls = []
##    jangkauan =  range(1, n+1)
##    siap = 'from __main__ import kalangBersusuh'
##    for i in jangkauan:
##        print('i = ', i)
##        t = timeit.timeit('kalangBersusuh(' + str(i) +')', setup = siap, number = 1)
##        ls.append(t)
##    return ls
##
##n = 10
##LS = ujiKalangBersusuh(n)
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()
##
###NOMOR 3F
##import timeit
##import matplotlib.pyplot as plt
##
##def kalangBersusuh(n):
##    for i in range(n):
##        for j in range(i):
##            for k in range(j):
##                m = i + j + k + 2019
##
##def ujiKalangBersusuh(n):
##    ls = []
##    jangkauan =  range(1, n+1)
##    siap = 'from __main__ import kalangBersusuh'
##    for i in jangkauan:
##        print('i = ', i)
##        t = timeit.timeit('kalangBersusuh(' + str(i) +')', setup = siap, number = 1)
##        ls.append(t)
##    return ls
##
##n = 10
##LS = ujiKalangBersusuh(n)
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()
##
###NOMOR 3G
##import timeit
##import matplotlib.pyplot as plt
##
##def kalangBersusuh(n):
##    for i in range(n):
##        if i % 3 == 0:
##            for j in range(n // 2):
##                j += j
##        elif i % 2 == 0:
##            for j in range(5):
##                j += j
##        else :
##            for j in range(n):
##                j += j
##
##def ujiKalangBersusuh(n):
##    ls = []
##    jangkauan =  range(1, n+1)
##    siap = 'from __main__ import kalangBersusuh'
##    for i in jangkauan:
##        print('i = ', i)
##        t = timeit.timeit('kalangBersusuh(' + str(i) +')', setup = siap, number = 1)
##        ls.append(t)
##    return ls
##
##n = 10
##LS = ujiKalangBersusuh(n)
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()
