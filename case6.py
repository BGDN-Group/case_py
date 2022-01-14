#!/usr/bin/python3

import random

print("1 — дециметр, 2 — километр, 3 — метр, 4 — миллиметр, 5 — сантиметр")

i = random.randrange(1,5)
N = random.randrange(1,10000)

print("Номер единицы длины: ", i)
print("Длина: ", N, end="")

if i == 1:
    print(" дм")
    print("В метрах: ",N/10)
elif i == 2:
    print(" км")
    print("В метрах: ",N*1000)
elif i == 3:
    print(" м")
    print("В метрах: ",N)
elif i == 4:
    print(" мм")
    print("В метрах: ",N/1000)
elif i == 5:
    print(" см")
    print("В метрах: ",N/100)