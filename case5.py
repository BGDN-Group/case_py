#!/usr/bin/python3

import random

print("1 — сложение, 2 — вычитание, 3 — умножение, 4 — деление")

i = random.randrange(1,5)
A = random.randrange(-10,10)
B = random.randrange(-10,10)

print("Номер операции: ", i)
print("Число A: ", A)
print("Число B: ", B)

if B < 0:
    B_str = "("+str(B)+")"
else:
    B_str = str(B)
if i == 1:
    print(A, "+", B_str, "=", A+B)
elif i == 2:
    print(A, "-", B_str, "=", A-B)
elif i == 3:
    print(A, "*", B_str, "=", A*B)
elif i == 4:
    if B == 0:
        print("Деление на ноль неопределено")
    else:
        print(A, "/", B_str, "=", A/B)