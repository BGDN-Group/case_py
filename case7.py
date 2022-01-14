#!/usr/bin/python3

import random

print("1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер")

i = random.randrange(1,6)
M = random.randrange(1,10000)

print("Номер единицы массы: ", i)
print("Масса: ", M, end="")

if i == 1:
    print(" кг")
    m = M
elif i == 2:
    print(" мг")
    m = M / 1000000
elif i == 3:
    print(" г")
    m = M / 1000
elif i == 4:
    print(" т")
    m = M * 1000
elif i == 5:
    print(" ц")
    m = M * 100

print("В килограммах: ",m)