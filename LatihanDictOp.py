#operator Dictionary

data_dict = {
    'cup':'ucup surucup',
    'tong':'otong surotong',
    'dung':'dudung marudung'
}
#panjang dictionary
LENDICT = len(data_dict)
print(f'panjang dictionary : {LENDICT}')
#mengecek key exist atau tidak
KEY = 'cup'
CHECKKEY = KEY in data_dict
print(f'apakah {KEY} ada di data_dict: {CHECKKEY}')
#mengakses value (read)
print(data_dict["cup"])
print(data_dict.get('cup'))
print(data_dict.get('kis','key tidak ditemukan'))