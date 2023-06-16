data0 = [1,2]
data1 = [3,4,5]

dataList = [1,2,3,4]

print(f'list biasa = {dataList}')

list2D = [data0,data1]

print(f'list 2D = {list2D}')

peserta0 = ['Ucup',25,'Laki-Laki']
peserta1 = ['Wardah',17,'Perempuan']
peserta2 = ['Kratos',42,"Laki-Laki"]

listPeserta = [peserta0,peserta1,peserta2]

print(f'Peserta = {listPeserta}')

for peserta in listPeserta:
    print(f'Nama\t: {peserta[0]}')
    print(f'Umur\t: {peserta[1]}')
    print(f'Gender\t: {peserta[2]}\n')