#!/usr/bin/python3

import random
import math

r = {1 : "катет a", 2 : "гипотенуза c", 3 : "высота h", 4 : "площадь S "}
d = []

i = random.randrange(1,5)

#i = 4
print("i : ", i)

N = random.randrange(1,100)
#N = 64

print(r[i],":",N)

if i == 1:
    a = N
    c = math.sqrt(2) * a
    h = c / 2
    S = c * h / 2
elif i == 2:
    c = N
    a = c / math.sqrt(2)
    h = c / 2
    S = c * h / 2
elif i == 3:
    h = N
    c = 2 * h
    a = c / math.sqrt(2)
    S = c * h / 2
elif i == 4:
    S = N
    c = math.sqrt(S * 4)
    a = c / math.sqrt(2)
    h = c / 2

d.append(a)
d.append(c)
d.append(h)
d.append(S)

print()
print("Элементы равнобедренного прямоугольного треугольника:")

for i in range(0,4):
    print(r[i+1],":",d[i])