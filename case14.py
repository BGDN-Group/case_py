#!/usr/bin/python3

import random
import math

r = {1 : "сторона a", 2 : "радиус R1 вписанной окружности", \
     3 : "радиус R2 описанной окружности", 4 : "площадь S"}
d = []

i = random.randrange(1,5)
i = 4

print("i : ", i)

N = random.randrange(1,100)

#N = 64
print(r[i],":",N)

if i == 1:
    a = N
    R1 = a * math.sqrt(3) / 6
    R2 = R1 * 2
    S = a**2 * math.sqrt(3) / 4
elif i == 2:
    R1 = N
    a = R1 * 6 / math.sqrt(3)
    R2 = R1 * 2
    S = a**2 * math.sqrt(3) / 4
elif i == 3:
    R2 = N
    R1 = R2 / 2
    a = R1 * 6 / math.sqrt(3)
    S = a**2 * math.sqrt(3) / 4
elif i == 4:
    S = N
    a = math.sqrt(S * 4 / math.sqrt(3))
    R1 = a * math.sqrt(3) / 6
    R2 = R1 * 2

d.append(a)
d.append(R1)
d.append(R2)
d.append(S)

print()
print("Элементы равностороннего треугольника:")

for i in range(0,4):
    print(r[i+1],":",d[i])