#MODUL 6
#CINDI DILA APRILIANA_L200200106

#NOMOR 8

class Node():
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

def cetak(head):
    curr = head
    while curr is not None:
        try:
            print (curr.data)
            curr = curr.link
        except:
            pass

a = Node(2)
b = Node(5)
c = Node(6)
d = Node(8)
e = Node(18)
f = Node(7)
g = Node(25)

a.link = b
b.link = c
c.link = d
d.link = e
e.link = f
f.link = g

def mergeSort(A):
    linked = A
    try:
        daftar = []
        curr = A
        while curr:
            daftar.append(curr.data)
            curr = curr.link
        A = daftar
    except:
        A = A

    if len(A) > 1:
        mid = len(A) // 2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]

        mergeSort(separuhKiri)
        mergeSort(separuhKanan)

        i = 0;j=0;k=0
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

    for x in A:
        try:
            linked.data = x
            linked = linked.link
        except:
            pass

mergeSort(a)
cetak(a)
