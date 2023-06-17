data1 = 'Selamat Malam'
print('Normal = '+data1)
data1 = data1.upper()
print('UPPER = '+data1)
data1 = data1.lower()
print('lower = '+data1)

data2 = 'malam minggu'
apakah_lower = data2.islower()
print(data2 + ' is lower '+ str(apakah_lower))
apakah_upper = data2.isupper()
print(data2 + ' is lower '+ str(apakah_upper))

Judul1 = "It's Okay Not To Be Okay"
Judul2 = "It is Okay Not To Be Okay"
Judul3 = "It Is Okay Not To Be Okay"

cekJudul1 = Judul1.istitle();
print(Judul1+" is title = "+str(cekJudul1))

cekJudul2 = Judul2.istitle();
print(Judul2+" is title = "+str(cekJudul2))

cekJudul3 = Judul3.istitle();
print(Judul3+" is title = "+str(cekJudul3))

cekStart = Judul3.startswith('It')
print('Starts = '+str(cekStart))

cekEnd = Judul3.endswith('Okay')
print('Ends = '+str(cekEnd))


pisah = ['selamat','malam','semuanya']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' BISA '.join(pisah)
print(gabungan)

gabungan = 'selamatbisamalambisasemuanya'
print(gabungan.split('bisa'))

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10,'x')
print("'"+tengah+"'")

tengah = tengah.strip('x')
print("'"+tengah+"'")
