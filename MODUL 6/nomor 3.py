#MODUL 6
#CINDI DILA APRILIANA_L200200106

#NOMOR 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList(object):
    def __init__(self):
        self.head = None
        
    def printLinkedList(self):
        head = self.head
        while(head != None):
            print('' + str(head.data)+" => ", end = '')
            head = head.next
        print()
        
    def cari(self, yang_dicari):
        posisi = 1
        x = self.head
        while(True):
            if x.data != yang_dicari:
                x = x.next
                posisi += 1
            elif x == None:
                print(yang_dicari, "Apakah ada dalam data ?")
                return "Data tidak ada"
                break
            else:
                print(yang_dicari,"Apakah ada dalam data?")
                return "Data ada pada simpul ke-"+str(posisi)
                break
            
    def tambahDepan(self, head):
        tambah = Node(head)
        if self.head != None:
            tambah.next = self.head
        self.head = tambah
        
    def tambahAkhir(self, head):
        x = self.head
        tambah = Node(head)
        while(True):
            if self.head == None:
                self.head = tambah
            if x.next == None:
                x.next = tambah
                break
            else:
                x = x.next
                
    def tambah(self, head, posisi):
        sekarang = 0
        tambah = Node(head)
        x = self.head
        while x != None:
            if sekarang == posisi-2:
                tambah.next = x.next
                x.next = tambah
            elif posisi == 1:
                tambah.next = self.head
                self.head = tambah
                break
            elif x == None:
                break
            else:
                x = x.next
            sekarang +=1
            
    def hapus(self, posisi):
        sekarang =1
        x = self.head
        while x != None:
            if posisi ==1:
                x = x.next
                self.head = x
                break
            elif x.next == None and sekarang < posisi:
                break
            elif sekarang == posisi-1:
                x.next = x.next.next
            else:
                x = x.next
            sekarang +=1
            
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
            
A = LinkedList()
A.printLinkedList()
A.tambahDepan(31)
A.tambahDepan(12)
A.tambahAkhir(20)
A.tambah(8, 3)
A.printLinkedList()
A.cari(12)
A.hapus(2)
A.printLinkedList()
A.display()
