from ModuleMath import tambah as add
from ModuleMath import kali as opp
from ModuleMath import pangkat as pang

import ModuleMath as module_math

hasil_tambah = add(1,2,3,4,5)
print(f"Hasil Tambah = {hasil_tambah}")

hasil_kali = opp(1,2,3,4,5)
print(f"Hasil Kali = {hasil_kali}")

pangkat_2 = pang(3)
print(f"Hasil pangkat 2 dari {pangkat_2(10)}")

hasil_tambah_alias = module_math.tambah(1,2,3,4,5)
print(f"Hasil Tambah = {hasil_tambah_alias}")

hasil_kali_alias = module_math.kali(1,2,3,4,5)
print(f"Hasil Kali = {hasil_kali_alias}")

pangkat_2_alias = module_math.pangkat(3)
print(f"Hasil pangkat 2 dari {pangkat_2_alias(10)}")
