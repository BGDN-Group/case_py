#!/usr/bin/python3

import random

M = random.randrange(1,13)

month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

try:
    D_Max = month[M]
    D = random.randrange(1,D_Max+1)

    print("Дата:")
    print("Месяц: {0}. День: {1}".format(M,D))

    if D < D_Max:
        D += 1
    else:
        D = 1
        if M == 12:
            M = 1
        else:
            M +=1

    print("Следующая дата:")
    print("Месяц: {0}. День: {1}".format(M,D))

except KeyError as e:
    print('Ошибка')
    raise SystemExit