#import time
import Packages.MathModule
from Packages import PhysicModule
from Packages.PhysicModule import gaya as ayag
#t_star = time.time()

hasil_tambah_1 = Packages.MathModule.tambah(1,2,3,4,5)
print(f"Hasil tambah dari Packages = {hasil_tambah_1}")

gaya = PhysicModule.gaya(90,10)
print(f'Gaya = {gaya}')

gaya = ayag(80,10)
print(f'Gaya = {gaya}')
#t_end = time.time()

#print(f"Waktu Eksekusi = {t_end - t_star}")