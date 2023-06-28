'''Nilai Default Argument pada Fungsi'''

def say_hello(name = "Ganteng"):
    '''fungsi say hello'''
    print(f'Hallo {name}')

say_hello("ucup")
say_hello()

def sapa_dia(nama,pesan = "Mau Kemana ?"):
    '''fungsi dengan satu input biasa dengan input default'''
    print(f'hai {nama}, {pesan}')

sapa_dia("dudung",'Udah Makan Belum ?')
sapa_dia('ucup')

def hitung_pangkat(angka,pangkat=2):
    hasil = angka ** pangkat
    return hasil
print(hitung_pangkat(5,2))

soal1 = hitung_pangkat(angka=5,pangkat=3)
print(soal1)

def fungsi(angka1=1,angka2=2,angka3=3,angka4=4,angka5=5):
    return angka1 + angka2 + angka3 + angka4 + angka5
print(fungsi())
print(fungsi(angka5=10))