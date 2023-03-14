#MODUL 4
#CINDI DILA APRILIANA_L200200106

#Nomor 5
class Node():
    def __init__(self, data, link=None):
        self.data = data
        self.next = link
        
    def cariItem(self, cari):
        x = self
        awal = 1
        while x != None:
            if x.data == cari:
                return "Item berada di simpul ke - " + str(awal)
            else:
                awal += 1
                x = x.next
        return "Item tidak ditemukan"
 
a = Node(10)
a.next = Node(15)
a.next.next = Node(20)
