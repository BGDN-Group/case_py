#!/usr/bin/python3

import random
import math

r = {1 : "радиус R", 2 : "диаметр D", 3 : "длина L", 4 : "площадь круга S"}
c = []
i = random.randrange(1,5)

#i = 4
print("i : ", i)

N = random.randrange(1,100)
print(r[i],":",N)

if i == 1:
    R = N
    c.append(R)
    c.append(2 * R)
    c.append(2 * math.pi * R)
    c.append(math.pi * R**2)

elif i == 2:
    D = N
    R = D / 2
    c.append(R)
    c.append(D)
    c.append(math.pi * D)
    c.append(math.pi * R**2)

elif i == 3:
    L = N
    R = L / 2 / math.pi
    c.append(R)
    c.append(2 * R)
    c.append(L)
    c.append(math.pi * R**2)

elif i == 4:
    S = N
    R = math.sqrt(S / math.pi)
    c.append(R)
    c.append(2 * R)
    c.append(2 * math.pi * R)
    c.append(S)

print()
print("Элементы окружности:")
for i in range(0,4):
    print(r[i+1],":",c[i])