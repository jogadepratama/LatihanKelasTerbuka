'''Latihan Fungsi'''

import os

def header():
    '''fungsi header'''
    os.system('cls')
    print (f"{'Program Menghitung Luas':^40}")
    print (f"{'Dan Keliling Persegi Panjang':^40}")
    print (f"{'='*40:^40}")

def pilihan():
    print (f"{'1. Hitung Panjang':<10}")
    print (f"{'2. Hitung Keliling':<10}")
    opsi = int(input("Pilih Program : "))
    return opsi

def inputUser():
    '''fungsi input user'''
    lebar = int(input("Masukan nilai lebar = "))
    panjang = int(input("Masukan nilai panjang = "))
    return lebar,panjang

def hitungLuas(panjang,lebar):
    '''fungsi hitung luas'''
    return lebar*panjang

def hitungKeliling(panjang,lebar):
    '''fungsi hitung keliling'''
    return 2*(lebar+panjang)

def hasil(pesan,jumlah):
    print (f"Hasil Perhitungan {pesan} = {jumlah}")

while True:
    header()
    OPSI = pilihan()
    if OPSI  == 1:
        LEBAR,PANJANG = inputUser()
        LUAS = hitungLuas(LEBAR,PANJANG)
        hasil("Luas", LUAS)
    elif OPSI == 2:
        LEBAR,PANJANG = inputUser()
        KELILING = hitungKeliling(LEBAR,PANJANG)
        hasil("Keliling", KELILING)
    else:
        print("Tidak Ada Pilihan Tersebut else")
        continue 

    EndProg = input("Melanjutkan Program (y/n) ? ")
    if EndProg == "n":
        break

print("Program Selesai, Terimakasih")