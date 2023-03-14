#MODUL 1
#CINDI DILA APRILIANA_L200200106

#NOMOR 11

def apakahKabisat(tahun):
    if tahun%4 == 0:
        if tahun%4 == 0 and tahun%100 != 0:
            return True
        elif tahun%100 == 0 and tahun%400 != 0:
            return False
        elif tahun%100 == 0 and tahun%400 == 0:
            return True
    else:
        return False
