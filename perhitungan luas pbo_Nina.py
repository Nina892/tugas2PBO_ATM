#NINA D0221112 INFORMATIKA H

print('''1.peregi
2.ligkaran
3.segitiga
ketik 4 untuk berhenti ! ''')
pilihan=0
while pilihan != 4:
    pilihan = int(input("masukkan pilihan : "))
    if pilihan ==1:
        sisi=float(input("masukkan sisi : "))
        luas=sisi*sisi
        print("luas dari persegi adalah " ,luas, " cm")
    elif pilihan ==2:
        phi = 3.14
        r = float(input("masukkan jari-jari : "))
        luas = phi*r**2
        print("luas dari lingkaran adalah ", luas, " cm")
    elif pilihan ==3:
        a = float(input("masukkan alas : "))
        t = float(input("masukkan tinggi : "))
        luas = 1/2 * a * t
        print("luas dari segitga adalah " , luas, " cm")
    elif pilihan ==4:
        break
    else:
        print(" periksa kembali inputan anda ")
