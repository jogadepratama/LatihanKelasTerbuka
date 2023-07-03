'''Lamda Funct'''

def f_kuadrat(angka):
    return angka**2

print(f"Hasil dari fungsi kuadrat = {f_kuadrat(5)}")

kuadrat = lambda angka:angka**2
print(f"Hasil dari lambda kuadrat = {kuadrat(5)}")

pangkat = lambda ang,pow:ang**pow
print(f"Hasil dari lambda pangkat = {kuadrat(5)}")

#sort list
data_list = ["Otong","Ucup","Dudung"]
data_list.sort()
print(f"Sorted List = {data_list}")

def byPangjang_Nama(nama):
    return len(nama)

data_list.sort(key = byPangjang_Nama)
print(f"Sorted list by panjang dengan fungsi = {data_list}")

data_list = ["Otong","Ucup","Dudung"]
data_list.sort(key = lambda nama:len(nama))
print(f"Sorted list by panjang dengan lamda = {data_list}")

data_angka = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def kurang_dari_lima(angka):
    return angka < 5
new_data = list(filter(kurang_dari_lima,data_angka))
print (new_data)
new_data = list(filter(lambda x:x>5,data_angka))
print (new_data)

data_genap = list(filter(lambda x:(x%2==0),data_angka))
print(data_genap)

data_ganjil = list(filter(lambda x:(x%2 != 0),data_angka))
print(data_ganjil)

data_3 = list(filter(lambda x:(x%3==0),data_angka))
print(data_3)

# Anonymous Function
# Currying <- Haskell Curry

def pankat(angka,n):
    hasil = angka**n
    return hasil
data_hasil = pangkat(5,2)
print(f"Fungsi Biasa = {data_hasil}")

def fPangkat(n):
    return lambda angka:angka**n

fPangkat1 = fPangkat(3)
print(f"Pangkat 1 = {fPangkat1(5)}")

fPangkat2 = fPangkat(7)
print (f"Pangkat 3 = {fPangkat2(6)}")
print (f"Pangkat Bebas = {fPangkat(5)(5)}")