'''Function with Return'''

'''
def namaFungsi(argument):
    badan fungsi
    return output
'''

def kuadrat(angka):
    '''Fungsi Kuadrat'''
    hasil = angka**2
    return hasil

print(kuadrat(9))

y = 10 + kuadrat(4)
print(y)

def fungsi_tambah(angka1,angka2):
    return angka1 + angka2
print(fungsi_tambah(2,242))

def operasiAritmatika(angka1,angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2

    return tambah,kurang,kali,bagi
k,l,m,n = operasiAritmatika(200,800)

print(f'Hasil dari tambah = {k}')
print(f'Hasil dari kurang = {l}')
print(f'Hasil dari kali = {m}')
print(f'Hasil dari bagi = {n}')