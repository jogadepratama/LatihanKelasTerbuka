manteman = {
    "Ucup":"Ucup Surucup",
    "tong":"Otong Morotong",
    "Asep":"Asep Markusep",
    "Acuy":"Acuy Surucuy"
}

for teman in manteman:
    print(teman)

keys = manteman.keys()
print("\nMenggunakan method keys")
print(keys,"\n")

for key in manteman.keys():
    print(manteman.get(key))

print("\nMenggunakan method Values\n")

values = manteman.values()
print(values,"\n")

for value in manteman.values():
    print(value)

print("\nMenggunakan method Items\n")

items = manteman.items()
print(items)

for item in manteman.items():
    print(item)

for key,value in manteman.items():
    print(f"key = {key} , Value = {value}")