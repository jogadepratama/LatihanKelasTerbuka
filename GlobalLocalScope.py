# Global dan Local Scope

var_global = "Otong"

#Akses Variable Global kedalam Fungsi
def fungsi1():
    print(f"Fungsi menampilkan variable Global = {var_global}")

fungsi1()

#Akses Variable Global di dalam Loop

for i in range(0,5):
    print(f"Var Global ke {i} - {var_global}")

#Akses Variable Global di dalam Percabangan
if True:
    print(f"Menampilkan Var Global di dalam Percabangan")

# Variable Local Scope
def fungsi2():
    variable_local = "Ucup" # <- Ini Adalah Variable Local SCope
fungsi2()
# print(variable_local) #Tidak bisa di lakukan

def fungsi3():
    print(f"Hello {nama}")
nama = "Otong"

fungsi3()

# Merubah Variable Local menjadi Global di dalam fungsi

number = 200
nama = "Ucup Surucup"

def fungsi4(namaBaru,nomorBaru):
    global number
    global nama
    nama = namaBaru
    number = nomorBaru

print(f"Sebelum {number,nama}")
fungsi4("Margonda",300)
print(f"Sebelum {number,nama}")

exnumber = 0

for i in range(0,4):
    exnumber += i
    exnumber_dummy = 0

print(exnumber)
print(exnumber_dummy)

if True:
    exnumber = 200
    exnumber_dummy = 300

print(exnumber)
print(exnumber_dummy)