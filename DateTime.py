#Date and Time
import datetime as dt

hari_ini = dt.date.today()

print(hari_ini)

tanggal = dt.date(2015,8,24)
print(tanggal)

print(5*'='+'INPUT TANGGAL LAHIR'+5*'=')
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f'Tanggal lahir anda adalah : {tanggal_lahir:}')
print(f'Harinya Adalah : {tanggal_lahir:%A}')

hari_ini = dt.date.today()
print(f'hari ini tanggal : {hari_ini}')
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
umur_hari_sisa = (umur_hari.days%30)
print(f"hari nya adalah  = {tanggal_lahir:%A}")
print(f"Umur anda adalah = {umur_tahun} tahun, {umur_bulan_sisa} bulan, {umur_hari_sisa} hari")

'''
import datetime as td

def calculate_days(start_date, end_date):
    date_format = "%Y-%m-%d"
    start_date = td.datetime.strptime(start_date, date_format)
    end_date = td.datetime.strptime(end_date, date_format)
    time_delta = end_date - start_date
    return time_delta.days

# Example usage
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

result = calculate_days(start_date, end_date)
print("The number of days between the two dates is:", result)
'''