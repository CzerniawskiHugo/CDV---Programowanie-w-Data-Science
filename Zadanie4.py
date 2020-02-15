# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:11:02 2020

@author: Hugo
"""

import cmath as cm

print('Zadanie nr4: Znajdowanie miejsc zerownych trojmianu kwadratowego')

a =int(input('Wprowadz wartosc dla liczby a: '))
b =int(input('Wprowadz wartosc dla liczby b: '))
c = int(input('Wprowadz wartosc dla liczby c: '))

def licz(a, b, c):
    wynik1 = (-b+cm.sqrt(b*b-4*a*c))/(2*a)
    wynik2 = (-b-cm.sqrt(b*b-4*a*c))/(2*a)
    return wynik1, wynik2

print(licz(a, b, c))
