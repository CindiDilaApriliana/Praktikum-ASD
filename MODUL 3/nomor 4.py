#MODUL 3
#CINDI DILA APRILIANA_L200200106

#NOMOR 4
class Node(object):
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
class DoubleList(object):
    def __init__(self):
        self.head = None
    def cetakSemua(self):
        head = self.head
        while head != None:
            print(head.data, end=' -> ')
            if head.next != None:
                head = head.next
            else:
                break
        print()
        while self.head != None:
            print(head.data, end=' -> ')
            if head.prev != None:
                head = head.prev
            else:
                break
        print()
        
    def tambahSimpulAwal(self, head):
        x = self.head
        tambah = Node(head)
        if x == None:
            self.head = tambah
        else:
            x.prev = tambah
            tambah.next = x
            self.head = tambah
            
    def tambahSimpulAkhir(self, head):
        x = self.head
        tambah = Node(head)
        while True:
            if x == None:
                self.head = tambah
                break
            elif x.next == None:
                x.next = tambah
                tambah.prev = x
                break
            else:
                x = x.next
z = DoubleList()
z.cetakSemua()
z.tambahSimpulAwal(8)
z.tambahSimpulAkhir(30)
z.tambahSimpulAkhir(12)
z.cetakSemua() 
