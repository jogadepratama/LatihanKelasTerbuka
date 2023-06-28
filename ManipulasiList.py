dataList = ["Ucup","dadang","awa"]

print(dataList[1])
print(dataList[0])
print(dataList[-3])

print(f"Panjang data List {len(dataList)}")

print(f'Data sebelum di tambah =\n{dataList}')
dataList.insert(0,"asep")
print(f'Data sesudah di tambah =\n{dataList}')
dataList.append("Londry")
print(f'Data sesudah di tambah =\n{dataList}')

dataListBaru = ["Malam","Baju","Celana"]
dataList.extend(dataListBaru)
print(f'Data gabungaan=\n{dataList}')

dataList[2] = "Rabu"
print(f'Data rubah=\n{dataList}')

dataList.remove("Rabu")
print(f'Data remove=\n{dataList}')

dataList.pop()
print(f'Data baru=\n{dataList}')