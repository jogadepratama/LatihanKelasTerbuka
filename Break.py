#Break

print(10*"="+"Contoh Pertama"+"="*10)
angka = 0

while angka <5:
    angka += 1
    print (f"Count -> {angka}")

    if angka == 3:
        print ("Nice !")
        break

    print ("Wassup !")
print("Akhir Dari Program")

print(10*"="+"Contoh Kedua"+"="*10)

data_int = int(input("Hitung Sampai = "))
angka = 0

while True:
    angka += 1
    print (f"Count -> {angka}")

    if angka == data_int:
        print ("Nice !")
        break

    print ("Wassup !")
print("Akhir Dari Program")