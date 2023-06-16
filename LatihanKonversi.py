print("\nPROGRAM KONVERSI TEMPERATUR\n")


data_suhu = float(input('Masukan suhu : '))

print("\n====CELCIUS====\n")
print('suhu adalah',data_suhu,'Celcius')

reamur = (4/5) * data_suhu
print('suhu dalam reamur adalah',reamur,'reamur')

fahrenheit = ((9/5)*data_suhu)+32
print('suhu dalam fahrenheit adalah',fahrenheit,'fahrenheit')

kelvin = data_suhu+273
print('suhu dalam kelvin adalah',kelvin,'kelvin')

rankine = (data_suhu+273.15)*(9/5)
print('suhu dalam rankine adalah',rankine,'rankie')

print("\n====FAHRENHEIT====\n")
#fahrenheit = float(input('Masukan suhu dalam fahrenheit : '))
print('suhu adalah',data_suhu,'fahrenheit')

celcius = (data_suhu-32)*(5/9)
print('suhu dalam celcius adalah',celcius,'celcius')

kelvin = (data_suhu+459.67)*(5/9)
print('suhu dalam kelvin adalah',kelvin,'kelvin')

reamur = (data_suhu-32)*(4/9)
print('suhu dalam reamur adalah',reamur,'reamur')

rankine = data_suhu+459.67
print('suhu dalam rankine adalah',rankine,'rankie')


print("\n====Reamur====\n")
#reamur = float(input('Masukan suhu dalam reamur : '))
print('suhu adalah',data_suhu,'reamur')

celcius = data_suhu/0.8
print('suhu dalam celcius adalah',celcius,'celcius')

kelvin = data_suhu/0.8+273.15
print('suhu dalam kelvin adalah',kelvin,'kelvin')

fahrenheit = data_suhu*2.25+32
print('suhu dalam fahrenheit adalah',fahrenheit,'fahrenheit')

rankine = (data_suhu*2.25)+491.67
print('suhu dalam rankine adalah',rankine,'rankie')

print("\n====Kelvin====\n")
#kelvin = float(input('Masukan suhu dalam kelvin : '))
print('suhu adalah',data_suhu,'kelvin')

celcius = data_suhu - 273.15
print('suhu dalam celcius adalah',celcius,'celcius')

reamur = (4/5)*(data_suhu - 273)
print('suhu dalam reamur adalah',reamur,'reamur')

fahrenheit = (data_suhu*9/5) - 459.67
print('suhu dalam fahrenheit adalah',fahrenheit,'fahrenheit')

rankine = data_suhu*9/5
print('suhu dalam rankine adalah',rankine,'rankie')

print("\n====Rankine====\n")
#rankine = float(input('Masukan suhu dalam rankine : '))
print('suhu adalah',data_suhu,'rankine')

celcius = (data_suhu - 491.67)*(5/9)
print('suhu dalam celcius adalah',celcius,'celcius')

fahrenheit = data_suhu - 459.67
print('suhu dalam fahrenheit adalah',fahrenheit,'fahrenheit')

kelvin = data_suhu*5/9
print('suhu dalam kelvin adalah',kelvin,'kelvin')

reamur = ((data_suhu/1.8)+273.15)*0.8
print('suhu dalam reamur adalah',reamur,'reamur')
