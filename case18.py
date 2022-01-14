#!/usr/bin/python3

import random

edinici  = {
    1 : 'один',
    2 : 'два',
    3 : 'три',
    4 : 'четыре',
    5 : 'пять',
    6 : 'шесть',
    7 : 'семь',
    8 : 'восемь',
    9 : 'девять'
}

dcat = {
    11 : 'одиннадцать',
    12 : 'двенадцать',
    13 : 'тринадцать',
    14 : 'четырнадцать',
    15 : 'пятнадцать',
    16 : 'шестнадцать',
    17 : 'семнадцать',
    18 : 'восемнадцать',
    19 : 'девятнадцать',
}

desyatki = {
    10 : 'десять',
    20 : 'двадцать',
    30 : 'тридцать',
    40 : 'сорок',
    50 : 'пятьдесят',
    60 : 'шестьдесят',
    70 : 'семьдесят',
    80 : 'восемьдесят',
    90 : 'девяносто',
}

sotni = {
    100 : 'сто',
    200 : 'двести',
    300 : 'триста',
    400 : 'четыреста',
    500 : 'пятьсот',
    600 : 'шестьсот',
    700 : 'семьсот',
    800 : 'восемьсот',
    900 : 'девятьсот',
}

try:
    N = random.randrange(100,999)
    #N = 911
    propis = ''
    print("N = ",N)
    q = int(N/100)*100
    propis += sotni[q]
    #print(propis)
    N -= q 
    if 10 < N and N < 20:
        propis += ' ' + dcat[N]
    else:
        r = N%10
        #print("r = ",r)
        q = int(N/10)*10
        #print("q = ",q)
        if q !=0:
            propis += ' ' + desyatki[q]
        if r != 0:
            propis += ' ' + edinici[r]
    print(propis)

except KeyError as e:
    print('Ошибка',e)
    raise SystemExit