import time
start_time = time.time()

print ("Hello World")
a = 100
b = 200
c = 300
panjang =  4000

print (a)
print (b)
print (a+start_time)
print (panjang)

for i in range(1,100):
    z = 1000
print (z)

a = (time.time() - start_time, "detik")
print (a)


Data_Interger = 1000
print ("data :", Data_Interger)
print ("- data bertipe :", type(Data_Interger))


Data_float = 243.5
print ("data :", Data_float)
print ("- data bertipe :", type(Data_float))

Data_String = "awa"
print ("data :", Data_String)
print ("- data bertipe :", type(Data_String))


Data_Bool = False
print ("data :", Data_Bool)
print ("- data bertipe :", type(Data_Bool))

from ctypes import c_double,c_long,c_char

Data_C_Double = c_double(10.5)
print ("data :", Data_C_Double)
print ("- data bertipe :", type(Data_C_Double))
