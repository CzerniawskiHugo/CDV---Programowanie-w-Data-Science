# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:16:20 2020

@author: Hugo
"""

import math


print('Zadanie nr11: Obliczenie silni iteracyjnie i rekurencyjnie: ')

def silnia(n):
    wynik = 1
    for i in range (1, n+1):
        wynik = wynik * i
    return wynik


print(silnia(4))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * math.factorial(n-1)





print('Ten program podaje silnie dla wybranego elementu. ')

n = int(input('Podaj element: '))

print(factorial(n))