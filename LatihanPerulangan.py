#Perulangan (loop)


angka2_list = [0,1,2,3,4]
print(angka2_list)

for i in angka2_list:
    print(f'i sekarang = {i}')

print('Akhir dari program 1 \n')

angka2_range = range(5)

for i in angka2_range:
    print(f'i sekarang = {i}')

print('Akhir dari program 2 \n')

angka2_range = range(1,5)

for i in angka2_range:
    print(f'i sekarang = {i}')

print('Akhir dari program 3 \n')

data_string = "Selamat Siang Jakarta"

for i in data_string:
    print (i)

print('Akhir dari program 4 \n') 

# While loop

angka = 0
print (f'angka sekarang -> {angka}')

while angka <10:
    angka += 1
    print (f'{angka} + 1 = {angka}')
    print (f'angka sekarang -> {angka}')

print('akhir dari program 5\n')