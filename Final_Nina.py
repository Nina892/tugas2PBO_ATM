# Nama : Nina
# NIM : D0221112

import math

class BangunRuang:
    def volume(self):
        pass

    def luas(self):
        pass

    def tampil1(self):
        print("Volume : ", self.volume())

    def tampil2(self):
        print("Luas : ", self.luas())

class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def volume(self):
        v = self.panjang * self.lebar * self.tinggi
        return v

    def luas(self):
        l = 2 * (self.panjang * self.lebar + self.lebar * self.tinggi + self.panjang * self.tinggi)
        return l

class Tabung(BangunRuang):
    def __init__(self, jari_jari, tinggi):
        self.jari_jari = jari_jari
        self.tinggi = tinggi
    
    def volume(self):
        v = math.pi * (self.jari_jari ** 2) * self.tinggi
        return v
    
    def luas(self):
        l = 2 * math.pi * self.jari_jari * (self.jari_jari + self.tinggi)
        return l
    
class Kubus(BangunRuang):
    def __init__(self, sisi):
        self.sisi = sisi

    def volume(self):
        v = self.sisi**3
        return v

    def luas(self):
        l = 6 * (self.sisi**2)
        return l


while True:
    print("""1. Menghitung volume
2. Menghitung luas
3. Memberhentikan program""")
    a = int(input("Masukkan pilihan : "))
    print()
    if a == 1:
        while True:
            print("""Menghitung Volume
1. Balok
2. Tabung
3. Kubus
4. Kembali kemenu awal""")
            b = int(input("Masukkan pilihan :"))
            print()
            if b == 1:
                input1 = int(input("Masukkan panjang balok: "))
                input2 = int(input("Masukkan lebar balok: "))
                input3 = int(input("Masukkan tinggi balok: "))
                balok = Balok(input1,input2,input3)
                balok.tampil1()
            elif b == 2:
                input1 = int(input("Masukkan jari-jari tabung : "))
                input2 = int(input("Masukkan tinggi tabung : "))
                tabung = Tabung(input1,input2)
                tabung.tampil1()
            elif b == 3:
                input1 = int(input("Masukkan jari-jari tabung : "))
                kubus = Kubus(input1)
                kubus.tampil1()
            else:
                break
    elif a == 2:
        while True:
            print("""Menghitung Luas
1. Balok
2. Tabung
3. Kubus
4. Kembali ke menu awal""")
            b = int(input("Masukkan pilihan :"))
            print()
            if b == 1:
                input1 = int(input("Masukkan panjang balok: "))
                input2 = int(input("Masukkan lebar balok: "))
                input3 = int(input("Masukkan tinggi balok: "))
                balok = Balok(input1,input2,input3)
                balok.tampil2()
            elif b == 2:
                input1 = int(input("Masukkan jari-jari tabung : "))
                input2 = int(input("Masukkan tinggi tabung : "))
                tabung = Tabung(input1,input2)
                tabung.tampil2()
            elif b == 3:
                input1 = int(input("Masukkan jari-jari tabung : "))
                kubus = Kubus(input1)
                kubus.tampil2()
            else:
                break
    else:
        print("Program berhenti")
        break