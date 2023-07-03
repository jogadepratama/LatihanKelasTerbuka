'''**kwargs'''

def fungsi1(nama,tinggi,berat):
    '''fungsi standart'''
    print(f"{nama} mempunyai tinggi {tinggi}cm dan {berat}kg")

fungsi1("Ucup",185,95)

def fungsi2(**kwargs):
    '''fungsi kwargs'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} mempunyai tinggi {tinggi}cm dan {berat}kg")

fungsi2(nama = "Ucup",tinggi = 185,berat = 95)


def fungsi3(*args,**kwargs):
    '''fungsi double args dan kwargs'''
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs['option'] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("Tidak Ada Operasi")
    return output
hasil = fungsi3(1,2,3,4,option = "tambah")
print(hasil)
hasil = fungsi3(1,2,3,4,option = "kali")
print(hasil)