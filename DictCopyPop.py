manteman = {
    "cup":"Ucup Surucup",
    "tong":"Otong Morotong",
    "sep":"Asep Markusep",
    "cuy":"Acuy Surucuy",
    "dung":"Dudung Marudung"
}

print("="*10,"Method Copy di Dictionary","="*10)
friends = manteman.copy()

print(f"manteman: {manteman}\n")
print(f"friends: {friends}\n")

manteman["cup"] = "Ucup Markicup"
print(f"manteman: {manteman}\n")
print(f"friends: {friends}\n")

print("="*10,"Method Pop/PopItem di Dictionary","="*10)

dataTeman = friends.pop("cuy")
print(f"dataTeman: {dataTeman}\n")
print(f"friends: {friends}\n")

dataLast = friends.popitem()
print(f"dataLast: {dataLast}\n")
print(f"friends: {friends}\n")