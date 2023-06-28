'''
sisi = 9

#Menggunakan for

print(10*"="+"Menggunakan for"+"="*10)
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print('Akhir Dari For \n')

print(10*"="+"Menggunakan while"+"="*10)
count = 1

while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break
print('Akhir Dari while \n')

print(10*"="+"Print Hanya Baris Ganjil"+"="*10)
count = 1
while True:  
    if (count%2):
        print("*"*count)
        count += 1
    else:
        count += 1
        continue

    if count > sisi:
        break
print('Akhir Dari while \n')

print(10*"="+"Print Segitiga Sama Sisi"+"="*10)
count = 1
spasi = int(sisi/2)
while True:  
    if (count%2):
        print(' '*spasi,"+"*count)
        count += 1
        spasi -= 1
    else:
        count += 1
        continue

    if count > sisi:
        break

print('Akhir Segitiga Sama Sisi \n')

print(10*"="+"Print Ketupat"+"="*10)
count = 1
spasi = int(sisi/2)
while True:  
    if (count%2):
        print(' '*spasi,"+"*count)
        count += 1
        spasi -= 1
    else:
        count += 1
        continue

    if count > sisi:
        break

while True:
    if (count%2): 
        spasi += 1
        print(" "*spasi,"+"*count)
        count -= 1
    else:
        count -= 1
    if count == 0:
        break

print('Akhir Ketupat \n')
'''
print(10*"="+"Print Ketupat versi simple"+"="*10)

for i in range(0, 5):
    print(" " * (5 - i), end = "")
    for x in range(i):
        print(" +", end = "")
    print()

for i in range(5, 0, -1):
    print(" "*(5-i),end='')
    for x in range(i):
        print(" +",end='')
    print()
