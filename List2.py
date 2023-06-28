list_buku = []
while True:
    print("\nMasukan Data Buku\n")
    judul = input("Judul buku \t: ")
    penulis = input("Nama Penulis \t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    print  ("\n\n","="*10,"DATA BUKU","="*10)
    for index,buku in enumerate(list_buku):
        print(f'{index+1} | {buku[0]} | {buku[1]}')
    
    print  ("\n\n","="*20)
    isLanjut = input("Apakah Masih Input Data (y/n) : ")

    if isLanjut == "n":
        break
print("PROGRAM SELESAI")