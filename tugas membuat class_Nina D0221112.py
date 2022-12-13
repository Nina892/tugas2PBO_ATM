class Kubus():
    def __init__(self,sisi):
        self.sisi = sisi

    def volume (self):
        vol_kub =self.sisi**3
        print("volume kubus adalah: " ,vol_kub)
    def luas (self):
        l_k =6* self.sisi**2
        print("luas kubus adalah: ", l_k)

class Tabung():
    def __init__(self,jari,tinggi):
        self.jari= jari
        self.tinggi= tinggi
    def volume (self):
        vol_t= 22/7 *self.jari**2 *self.tinggi
        print("volume tabung adalah: ", vol_t)
    def luas (self):
        l_t= 2*22/7*self. jari(self.jari+self.yinggi)

class Balok():
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
    def volume (self):
        vol_b = self.panjang*self.lebar*self.tinggi
        print("volume balok adalah : " , vol_b)
    def luas (self):
        l_b = 2 * (self.panjang * self.lebar + self.lebar * self.tinggi + self.panjang * self.tinggi)
        print("luas balok adalah: " , l_b)

while True:
    print()
    print('''bangun ruang yang akan di hitung:
1.kubus
2.Tabung
3.Balok''')
    pilihan = input ("-->")

    if pilihan == '1':
        k= float(input("Masukkan sisi:"))
        kubus = kubus(k)
        print()
        prit('''Masukkan angka 1 atau 2 untuk mengitung salah satunya
1. mengitung volume
2. menghitung luas''')
        pilihan = input("-->")
        if pilihan =="1":
            kubus.volume()
        elif pilihan =="2":
            kubus.luas()
        else:
            break
    elif pilihan == '2':
        j= float(input("Masukkan jari: "))
        t= float(input("Masukkan tinggi: "))
        tabung = Tabung(j,t)
        print()
        print('''Masukkan angka 1 atau 2 untuk mengitung salah satunya
1. mengitung volume
2. menghitung luas''')
        pilihan = input("-->")
        if pilihan =="1":
            Tabung.volume()
        elif pilihan =="2":
            Tabung.luas()
        else:
            break
    elif pilihan == '3':
        p = float(input("Masukkan Panjang: "))
        l = float(input("Masukkan Lebar: "))
        t = float(input("Masukkan Tinggi: "))
        balok = Balok(p, l, t)
        print()
        print('''Ketik 1 atau 2 untuk menghitung salah satunya
1.Menghitung Volume
2. Menghitung Luas''')
        pilihan = input("-->")
        if pilihan == "1":
            balok.volume()
        elif pilihan == "2":
            balok.luas()
        else :
            break
    elif pilihan == '4':
        break
    else :
        print("inputan anda salah") 
        
        



    
        
