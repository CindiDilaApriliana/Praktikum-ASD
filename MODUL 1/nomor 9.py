#MODUL 1
#CINDI DILA APRILIANA_L200200106

#NOMOR 9

def kelipatan(x):
    for i in range(1,x+1):
        if i%3 == 0 and i%5 == 0:
            print("Python UMS")
        elif i%5 == 0:
            print("UMS")
        elif i%3 == 0:
            print("phyton")
        else:
            print(i)
