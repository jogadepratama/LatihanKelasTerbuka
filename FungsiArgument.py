''' Fungsi Argumen'''

'''
def nama_fungsi(argument):
    Badan Fungsi

'''

def hello_world(name):
    print(f'Selamat Datang Dunia {name}')

hello_world("Ucup")
hello_world("Asep")

def tambah(angka1,angka2):
    '''Fungsi Tambah'''
    hasil = angka1 + angka2
    print(f'{angka1} + {angka2} = {hasil}')

tambah(5,6)
tambah(584000,568441)

def sayHi(list_peserta):
    '''Fungsi Say Hi'''
    data_peserta = list_peserta.copy()
    for peserta in list_peserta:
        print(f'yang terhormat {peserta}')

daftar_peserta = ['ucup','marwa','kana']

sayHi(daftar_peserta)