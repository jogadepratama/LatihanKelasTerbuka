'''*args'''

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat badan {berat}")
fungsi("Ucup",175,95)

def fungsi2(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat badan {berat}")

fungsi2(["Marwa",210,98])

def fungsi3(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat badan {berat}")
fungsi3("Dudung",168,55)

def tambah(*data):
    output = 0
    for angka in data:
        output += angka
    return output

hasil = tambah(5,1,2,4,2,6,2,3,5,7,4,8,4,8,5,1,5,45)
print(hasil)

hasil = tambah(20,20,10)
print (hasil)