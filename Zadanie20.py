# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 20:49:18 2020

@author: Hugo
"""

print('Zadanie nr19: Program podaje nazwy miesiecy po angielsku: ')

Miesiace = {
        "Styczen" : ('January') ,
        "Luty" : ('February'),
        "Marzec" : ('March'),
        "Kwiecien" : ('April'),
        "Maj" : ('May'),
        "Czerwiec" : ('June'),
        "Lipiec" : ('July'),
        "Sierpien" : ('August'),
        "Wrzesien" : ('September'),
        "Pazdziernik" : ('October'),
        "Listopad" : ('November'),
        "Grudzien" : ('December')
         }

def dajMiesiac():
    x = Miesiace.get(str(input('Wprowadz nazwe miesiaca: ')))
    print('Angielska nazwa podanego miesiaca to: ')
    return  x 


def main():
    
    print(dajMiesiac())
    
    
    
if __name__ == '__main__':
    main()
        
        
        