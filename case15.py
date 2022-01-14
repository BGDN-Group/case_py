#!/usr/bin/python3

import random

_suit = {
    1 : 'пики',
    2 : 'треф',
    3 : 'бубен',
    4 : 'червей'
}

_value  = {
    6 : 'шестерка',
    7 : 'семерка',
    8 : 'восьмерка',
    9 : 'девятка',
    10 : 'десятка',
    11 : 'валет',
    12 : 'дама',
    13 : 'король',
    14 : 'туз'
}

try:
    N = random.randrange(6,15)

    print("Достоинство карты: ", N, "-", _value[N])

    M = random.randrange(1,5)

    print("Масть карты: ", M, "-", _suit[M])

    print("Карта: ", _value[N], _suit[M])
except KeyError as e:
    print('Ошибка')
    raise SystemExit