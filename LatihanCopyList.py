#Teknik Menduplikat list

a = ['ucup','otong','dudung']
print(f"a = {a}")

b = a
print(f'b = {b}')

a[1] = "Michael"
b.sort()

print(f"a = {a}")
print(f'b = {b}')

print(f'Address a = {hex(id(a))}')
print(f'Address a = {hex(id(b))}')

print('Membuat List C dengan a.copy()')
c = a.copy()

print(f'Address a = {hex(id(a))}')
print(f'Address b = {hex(id(b))}')
print(f'Address c = {hex(id(c))}')


print(f"a = {a}")
print(f'b = {b}')
print(f'c = {c}')

print(f'Kita ubah data di list C')
c[1] = "dadang"


print(f"a = {a}")
print(f'b = {b}')
print(f'c = {c}')