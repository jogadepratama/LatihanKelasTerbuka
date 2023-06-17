#KompirasiDataInput
'''
inputUser = float(input("Masukan Angka yang bernilai\nKurang dari 3\nLebih dari 10 \n: "))
isKurangDari = (inputUser < 3)
isLebihDari = (inputUser > 10)
isCorrect = isKurangDari or isLebihDari
print('Kurang Dari 3 = ',isKurangDari)
print('Lebih Dari 10 = ',isLebihDari)
print("Angka yang anda masukan = ", isCorrect)

print("\n",10*"=","\n")

inputUser = float(input("Masukan Angka yang bernilai\nlebih dari 3\nkurang dari 10 \n:"))
isKurangDari = (inputUser > 3)
isLebihDari = (inputUser < 10)
isCorrect = isKurangDari and isLebihDari
print("Lebih dari 3 = ", isKurangDari)
print("Kurang dari 10 = ", isCorrect)
print("Angka yang anda masukan = ", isCorrect)
'''
#SoalatihanKompirasiDataInput

inputData = float(input("Masukkan Angka : "))

hasil = 0<inputData<5 or 8<inputData<11
print ("Hasil :",hasil)

inputData = float(input("Masukkan Angka : "))

hasil = inputData<0 or 5<inputData>8 or 11<inputData
print ("Hasil :",hasil)