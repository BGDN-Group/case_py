#!/usr/bin/python3

import random

d = ['Север', 'Запад', 'Юг', 'Восток']
r = {-1 : "поворот направо", 1 : "поворот налево", 2 : "поворот на 180 градусов"}

try:
    i_bak = i = random.randrange(0,4)
    print("i : ", i)
    C = d[i]

    print("Исходное направление (C) : ", C)
    N1 = random.choice([-1,1,2])
    print("Команда 1 (N1) : ", N1)
    print("Поворот: ", r[N1])
    i = (4+i+N1)%4

    print("i : ", i)
    C = d[i]

    print("Новое направление (C) : ", C)
    N2 = random.choice([-1,1,2])
    print("Команда 2 (N2) : ", N2)
    print("Поворот: ", r[N2])

    i = (4+i+N2)%4
    print("i : ", i)
    C = d[i]
    
    print("Новое направление (C) : ", C)
    
    i_bak = (4+i_bak+N1+N2)%4
    print("i_bak : ", i_bak)
    C = d[i_bak]
    print("Новое направление (C) : ", C)
    
except KeyError as e:
    print('Ошибка')
    raise SystemExit