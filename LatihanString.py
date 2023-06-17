data = 'data string'
print(data, type(data))

str1 = 'Awa'
str2 = 'Maria'
str3 = "O'clock"

dataString = str1+' '+str2+' '+str3
print(dataString)
panjang = len(dataString)
print(panjang)

w = 'w'
status = w in dataString
print (w + 'ada di ' + dataString + '=' + str(status), type(status))

W = 'W'
status = W in dataString
print (W + ' ada di '+ dataString + ' = ' + str(status), type(status))

w = 'w'
status = w not in dataString
print (w + 'ada di ' + dataString + '=' + str(status), type(status))

print ("Urutan ke 4 = ", dataString[4])
print ("Urutan ke 10 = ", dataString[10])
print ("Urutan ke 0-7 = ", dataString[0:8])
print ("Urutan ke 5-11 = ", dataString[5:12])
print ("Urutan ke (2,4,6,8,10,12) = ", dataString[0:18:2])

print ("paling kecil : "+min(dataString))
print ("paling besar : "+max(dataString))

ascii_code = ord('M')
print('ASCI code =',str(ascii_code))

data = 256
print('ASCI code =',chr(data))

data = 'Awa Maria Renata'
jumlah = data.count("a")
jumlah = dataString.index('w')
print("Jumlah Karatek a = ",jumlah,str(jumlah))

