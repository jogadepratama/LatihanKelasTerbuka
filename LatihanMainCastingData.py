# Casting Data
# Merubah tipe data dari tipe data lain
# Case : String, Interger, Bolean, dan Float

print("====Tipe Data String====")
data_str = input("Input Data String :")
print("Data :",data_str, ", Tipe Data :",type(data_str))

data_int = int(data_str)#data_str harus angka
data_bool = bool(data_str)#Akan False ketika data_str kosong
data_float = float(data_str)#data_str harus angka

print("Data :",data_int, ", Tipe Data :",type(data_int))
print("Data :",data_bool, ", Tipe Data :",type(data_bool))
print("Data :",data_float, ", Tipe Data :",type(data_float))

print("====Tipe Data Interger====")
data_int = input("Input Data Integer :")
print("Data :",data_int, ", Tipe Data :",type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)# Akan False ketika int = 0

print("Data :",data_float, ", Tipe Data :",type(data_float))
print("Data :",data_str, ", Tipe Data :",type(data_str))
print("Data :",data_bool, ", Tipe Data :",type(data_bool))

print("====Tipe Data Float====")
data_float = input("Input Data Float :")
print("Data :",data_float, ", Tipe Data :",type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)#  Akan False ketika Float = 0

print("Data :",data_int, ", Tipe Data :",type(data_int))
print("Data :",data_str, ", Tipe Data :",type(data_str))
print("Data :",data_bool, ", Tipe Data :",type(data_bool))

print("====Tipe Data Boolean====")
data_bool = bool(int(input("Input Data Float :")))
print("Data :",data_bool, ", Tipe Data :",type(data_bool))

data_int = int(data_bool)# Jika False = 0, True = 1
data_str = str(data_bool)
data_float = float(data_bool)# Jika False = 0.0, True = 1.0

print("Data :",data_int, ", Tipe Data :",type(data_int))
print("Data :",data_str, ", Tipe Data :",type(data_str))
print("Data :",data_float, ", Tipe Data :",type(data_float))

