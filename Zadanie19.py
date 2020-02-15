# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 20:49:18 2020

@author: Hugo
"""

print('Zadanie nr19: Program podaje iloć dni w miesiącu: ')

Miesiace = {
        "Styczen" : 31 ,
        "Luty" : 28,
        "Marzec" : 31,
        "Kwiecien" : 30,
        "Maj" : 31,
        "Czerwiec" : 30,
        "Lipiec" : 31,
        "Sierpien" : 31,
        "Wrzesien" : 30,
        "Pazdziernik" : 31,
        "Listopad" : 30,
        "Grudzien" : 31
         }

def dajMiesiac():
    x = Miesiace.get(str(input('Wprowadz nazwe miesiaca: ')))
    print('Ilosc dni we wskazanym miesiacu to: ')
    return  x 


def main():
    
    print(dajMiesiac())
    
    
    
if __name__ == '__main__':
    main()
        
        
        