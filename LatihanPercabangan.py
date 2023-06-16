#Latihan Percabangan
print(10*'=')
print("Kalkulator Sederhana")
print(10*'='+"\n")

angka1 = float(input('Masukan Angka Pertama = '))
operator = input("Operator (+,-,x,/) = ")
angka2 = float(input('Masukan Angka Kedua = '))

if operator == '+':
    hasil = angka1 + angka2
    print(f'Hasilnya adalah {hasil}')
elif operator == "-":
    hasil = angka1 - angka2
    print(f'Hasilnya adalah {hasil}')
elif operator == "x" or operator == '*':
    hasil = angka1 * angka2
    print(f'Hasilnya adalah {hasil}')
elif operator == "/":
    hasil = angka1 / angka2
    print(f'Hasilnya adalah {hasil}')
else:
    print("Masukan Angka Yang Benar!")

print ('Akhir dari program, Terimakasih')