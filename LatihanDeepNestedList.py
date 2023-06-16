data0 = [1,2]
data1 = [3,4]

data_2D = [data0,data1,10]
data_2D_copy = data_2D.copy()

print(f'data = {data_2D[0]}\n')
print(f'data = {data_2D[0][0]}\n')
print(f'data = {data_2D[0][1]}\n')
print(f'data = {data_2D[1]}\n')
print(f'data = {data_2D[1][0]}\n')
print(f'data = {data_2D[1][1]}\n')

print("="*10+"Copy Address List"+"="*10,"\n")

print(f"addres data_2D =  {hex(id(data_2D))}")
print(f"addres data_2D_copy =  {hex(id(data_2D_copy))}")

print("\nAddress dari member ke - 1\n")
print(f"addres data_2D =  {hex(id(data_2D[0]))}")
print(f"addres data_2D_copy =  {hex(id(data_2D_copy[0]))}")

data_2D[1][0] = 5
data_2D[2] = 9
print(f'data = {data_2D}')
print(f'data copy = {data_2D_copy}')