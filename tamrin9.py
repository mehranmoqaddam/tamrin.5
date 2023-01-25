import math
#moadele daraje 2 = ax2 + bx + c = 0

def moadeledaraje2():
    a = int(input("a>>not=0 : "))
    b = int(input("b : "))
    c = int(input("c : "))
    x_1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    x_2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    print("x sharte avval :",x_1)
    print("x sharte dovvom :",x_2)
moadeledaraje2()