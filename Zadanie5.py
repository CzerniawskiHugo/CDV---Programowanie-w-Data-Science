# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:41:50 2020

@author: Hugo
"""

print('Zadanie nr5: Sprawdz czy wprowadzona liczba jest dodatnia czy nie.')

x = float(input('Wprwadź liczbę do sprawdzenia: '))

def weryfikatorLiczbowy(x):
    
    if x < 0:
        return('Liczba mniejsza od 0')
    if x == 0:
        return('Liczba równa 0')
    else:
        return('Liczba większa od zera')
        
        
def main():
    print('Rezultat:')
    print(weryfikatorLiczbowy(x))
    
if __name__ == '__main__':
    main()
    
    
        
