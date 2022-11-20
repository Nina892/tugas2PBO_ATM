user_id=0
loop ="n"
users =[
    {
        "id": "1234",
        "no_rekening": "1234567890",
        "username": "Nina",
        "pin":"0708",
        "saldo":600000
    },
    
]
status_login = False
pakai_atm ="y"


def cek_login(p):
    for user in users:
        if user['pin'] == p:
            return user
        return False
    
def cek_user(id):
    for i in range(len(users)):

        if users[i]['id'] == str(id):
            return int(i)
        return-1
    
def cek_rekening(no):
    for i in range(len(users)):
        if str(users[i]['no_rekening'])== str(no):
            return int(i)
        return-1
    
def transfer_uang(uang,no_rekening):
    index1 = cek_user(user_id)
    index2 = cek_rekening(no_rekening)
    if index1 >=0:
        if users[index1]['saldo'] >= int(uang):
            users[index1]['saldo']= users[index1]['saldo'] - int(uang)
            users[index2]['saldo']= users[index2]['saldo'] + int(uang)
            print("Anda Berhasil mentransfer uang Rp." + str(uang) + "ke rekening" + no_rekening)
            print(" sisa saldo anda adalah Rp.", users[index1]['saldo'])
        else:
            print("saldo anda tidak cukup")
            
def ambil_uang(uang):
    index1 = cek_user(user_id)
    if index1 >=0:
        if users [index1]['saldo'] >= int(uang):
            users [index1]['saldo']= users[index1]['saldo'] - int(uang)
            print(" Anda berhasil menarik uang Rp." + str(uang))
            print(" Sisa saldo anda adalah Rp.", users[index1]['saldo'])
        else:
            print(" Saldo anda tidak cukup")
                
while pakai_atm == "y":
    while not status_login:
        print(" SELAMAT DATANG DI ATM BANK PESONAINFORMATIKA")
        print(" Silahkan Masukkan Pin Anda")
        pin = input("masukkan PIN: ")
        cl = cek_login(pin)
        if cl:
            print(" selamat datang " + cl['username'])
            user_id = cl['id']
            status_login = True
            loop = "y"
        else:
            print("")
            print("PIN anda salah")
            print("")
            print

    while loop == "y" and status_login:
        u = users[cek_user(user_id)]
        print(" SELMAT DATANG DI ATM PESONAINFORMATIKA ")
        print("1. cek saldo")
        print("2. transfer uang")
        print("3. ambil uang ")
        print("4. logout")
        print("5. keluar ATM")
        a = int(input(" silahkan pilih menu: "))
        if a == 1:
            print("")
            print("sisa saldo anda adalah Rp.", u['saldo'])
            print("")
            print("")
            loop ="n"
        elif a == 2:
            print("untuk mentransfer uang silahkan masukkan no rekening tujuan")
            no_rek = input("masukkan no rekening tujuan:")
            cnk = cek_rekening(no_rek)
            if cnk >=0:
                print("nomor rekening di temukan, silahkan masukkan nominal yang akan di transfer")
                nominal = input("nominal yang akan di transfer :")
                transfer_uang (nominal,
                       no_rek)
                print("")
                loop = "n"
            else:
                print("")
                print("nomor rekening tujuan tidak ditemukan atau tidak terdaftar")
                print("")
                loop = "n"
        elif a == 3:
            nominal = input("nominal yang akan di tarik :")
            ambil_uang(nominal)
            print("")
            loop = "n"
        elif a == 4:
            status_login = False
        elif a == 5:
            status_login = False
            loop = "n"
            pakai_atm ="n"
        else:
            print("pilih tidak tersedian")
        if status_login == True:
            input("kembali ke menu(Enter)")
            print("")
            loop = "y"
    
              
   
    
