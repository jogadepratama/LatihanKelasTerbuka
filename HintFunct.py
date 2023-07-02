'''Type Hints Pada Function'''
import string
def fungs(args1:int,args2:int) -> int:
    """Fungsi Dengan Hints"""
    output = args1**args2
    return output

hasil = fungs(5,4)
print(hasil)

def display(args:string):
    print(args)

display('Ucup')