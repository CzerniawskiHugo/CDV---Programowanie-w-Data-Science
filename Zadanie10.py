# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:17:45 2020

@author: Hugo
"""

import numpy as np


print('Zadanie nr10: Srednia i odchylenie standardowe ')

while 1==1:

    n = int(input('Wprowadz liczbe cyfr, z ktorych ma zostac wyliczona srednia: '))
    
    lista = []
    
    
    for i in range(n):
        lista.append(int(input('Wporwadz wartosci listy: ')))
        srednia = np.mean(lista)
        odchy_Stand = np.std(lista)
            
    
    
    
    
        
    
    print('Srednia wpisanych liczb = ' + str(srednia))
    print('Odchylenie standardowe podanych liczb = ' + str(odchy_Stand))
    
    wyjscie = input('Jesli chcesz zakonczyc, wprowadz slowo tak:  ' )
    
    if wyjscie == 'tak':
        break

