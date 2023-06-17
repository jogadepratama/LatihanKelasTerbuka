#String
nama = "Kastino"
format_str = f"Hallo ! {nama}"
print(format_str)

#float
angka = 2005.5
format_str = f'Angka = {angka}'
print(format_str)

#Bilangan Bulat
angka = 15
format_str = f'angka = {angka:d}'
print(format_str)

#Bilangan dengan ordo Ribuan
angka = 2000000
format_str = f'angka jutaan = {angka:,}'
print(format_str)

#float belakang koma
angka = 2005.541523
format_str = f'Angka = {angka:.2f}'
print(format_str)

#Menampilkan leading zero
angka = 2005.541523
format_str = f'Angka = {angka:010.3f}'
print(format_str)

#Menampilka angka + - plus minus
angka_minus = -10
angka_plus = 10

format_minus = f"minus = {angka_minus:+d}" 
format_plus = f"plus = {angka_plus:+d}"

print(format_minus)
print(format_plus)

#Memformat Persen
persentase = 0.39
format_persen = f"Persentase = {persentase:.2%}"
print(format_persen)

#Melakukan Operasi Aritmatika
Harga = 25000
jumlah = 132
format_string = f"Harga Total = Rp.{Harga*jumlah:,}"
print(format_string)

#format angka lain (binary octal hex)
angka = 153

format_bin = f"Binary = {bin(angka)}"
format_oct = f"Octal = {oct(angka)}"
format_hex = f"Hexadecimal = {hex(angka)}"

print(format_bin)
print(format_oct)
print(format_hex)