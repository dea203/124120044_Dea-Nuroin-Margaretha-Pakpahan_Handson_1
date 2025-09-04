username_benar = "nuroin"
password_benar = "halo"
percobaan = 0
maksimal = 3

while percobaan < maksimal: 
    username = input("username: ")
    password = input("password: ")
    
    if(username == username_benar and password == password_benar):
        print("Login Berhasil")
        break
    else:
        print("username/password salah")
        percobaan = percobaan + 1
        sisa = maksimal - percobaan
        if(sisa == 0):
            print("Akun Terkunci")

        