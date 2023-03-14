#MODUL 8
#CINDI DILA APRILIANA_L200200106

#Latihan 1

class Stack():
    def __init__(self):
        self.items =[]
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.items)
    def peek(self):
        assert not self.isEmpty(), "Stack kosong. Tidak bisa diintip."
        return self.items[-1]
    def pop(self):
        assert not self.isEmpty(), "Stack kosong. Tidak bisa di-pop."
        return self.items.pop()
    def push(self,data):
        self.items.append(data)
