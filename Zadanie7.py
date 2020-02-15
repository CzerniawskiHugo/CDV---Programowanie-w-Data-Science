# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:58:31 2020

@author: Hugo
"""

print('Zadanie nr7: program drukuje kazda litere odwrocenego stringa w osobnym wierszu ')



str = input('Wprowadz string, ktory chcialbys odwrocic: ')

string2 = ''

def odwracacz():

    for ch in range(0, len(str)):
        print(str[len(str) - 1 - ch])

def main():
    print('String do odwrocenia ' + str)
    odwracacz()

if __name__ == '__main__':
    main()


        

    
    