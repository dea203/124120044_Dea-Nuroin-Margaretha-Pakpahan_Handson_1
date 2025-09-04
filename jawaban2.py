harga = int (input("harga:"))

if(harga >= 100000):
    kupon = input("pakai kupon?")
    if(kupon == "iya"):
        potongan = harga * 20//100
        print("diskon:", potongan)
        total = harga - potongan
        print("total:", total)
    else:
        print("total:", harga)