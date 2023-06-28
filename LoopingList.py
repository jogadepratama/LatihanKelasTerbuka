#looping List

print("="*10,"For Loop","="*10)
dataList = [5,8,7,9,6,1,2,3,4]
for data in dataList:
    print(f'Angka di dalam list = {data}')

daftarList = ['ucup','awa','marni','budi','lemba','trap']
for peserta in daftarList:
    print(f"Data Peserta = {peserta}")

print("="*10,"For Loop and Range","="*10)

dataList = [5,8,7,9,6,1,2,3,4]
daftar = len(dataList)
for i in range(daftar):
    print(f"Data List = {dataList[i]}")

print("="*10,"While Loop","="*10)

dataList = [5,8,7,9,6,1,2,3,4]
daftar = len(dataList)
i = 0

while i < daftar:
    print(f"Data List = {dataList[i]}")
    i += 1

print("="*10,"List Comprehension","="*10)

data = ['ucup',5,74,7,8,6,"awa"]

[print (f"Data Compre = {i}") for i in data]
print
print("="*10,"Enumerate","="*10)

dataList = ['ucup',5,74,7,8,6,"awa"]

for index,data in enumerate(dataList):
    print(f'Index = {index} , Data = {data}')

print("="*10,"Contoh Fungsi","="*10)
data2 = [5,8,9,4,3,7,6,12,154,332]
dataKuadrat = [i**2 for i in data2]
print(dataKuadrat)