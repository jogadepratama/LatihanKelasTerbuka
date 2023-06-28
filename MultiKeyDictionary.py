import datetime

mahasiswa1 = {
    'nama':'Ucup Surucup',
    'nim':'190225401',
    'sks_lulus':130,
    'beasiswa':False,
    'Tanggal lahir':datetime.datetime(2001,4,10)
}

mahasiswa2 = {
    'nama':'Dadang Markidang',
    'nim':'190225402',
    'sks_lulus':144,
    'beasiswa':True,
    'Tanggal lahir':datetime.datetime(2000,10,10)
}

mahasiswa3 = {
    'nama':'Jerko Marjoke',
    'nim':'190225403',
    'sks_lulus':120,
    'beasiswa':False,
    'Tanggal lahir':datetime.datetime(2000,8,12)
}

mahasiswa4 = {
    'nama':'Samuel Etoo',
    'nim':'190225404',
    'sks_lulus':133,
    'beasiswa':True,
    'Tanggal lahir':datetime.datetime(2000,3,22)
}

dataMahasiswa = {
    "MAH001":mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3,
    'MAH004':mahasiswa4
}

print(f"Data Mahasiswa\n{'Key':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*50)

for mahasiswa in dataMahasiswa:
    KEY = mahasiswa
    NAMA = dataMahasiswa[KEY]["nama"]
    NIM = dataMahasiswa[KEY]["nim"]
    SKS = dataMahasiswa[KEY]["sks_lulus"]
    BEASISWA = dataMahasiswa[KEY]["beasiswa"]
    LAHIR = dataMahasiswa[KEY]["Tanggal lahir"].strftime('%x')

    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:<9} {LAHIR:<10}")
