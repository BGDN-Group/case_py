#!/usr/bin/python3

import random

M = random.randrange(1,13)

d = {'С' : 'Север', 'З' : 'Запад', 'Ю' : 'Юг', 'B' : 'Восток'}
r = {-1 : "поворот направо", 0 : "продолжать движение", 1 : "поворот налево"}
d1 = {0 : 'С', 1: 'З',  2 : 'Ю', 3 : 'B'}
try:
    i = random.randrange(0,4)
    #print("i : ", i)
    #print("d1 : ", d1[i])
    #print("d : ", d[d1[i]])
    C = d[d1[i]]
    print("Исходное направление (C) : ", C)
    N = random.randrange(-1,2)
    print("Команда (N) : ", N)
    print("Поворот: ", r[N])
    if N == -1:
        print("Part -1")
        if i == 0:
            i = 3
            #print("Part ", d[d1[i]])
        elif i == 3:
            i = 2
            #print("Part ", d[d1[i]])
        elif i == 2:
            i = 1
            #print("Part ", d[d1[i]])
        elif i == 1:
            i == 0
            #print("Part ", d[d1[i]])
    elif N == 1:
        #print("Part -1")
        if i == 0:
            i = 1
        elif i == 1:
            i = 2
        elif i == 2:
            i = 3
        elif i == 3:
            d1 = 0
    C = d[d1[i]]
    print("Новое направление (C) : ", C)

except KeyError as e:
    print('Ошибка')
    raise SystemExit