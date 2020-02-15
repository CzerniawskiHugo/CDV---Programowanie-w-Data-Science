# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:34:03 2020

@author: Hugo
"""

import matplotlib.pyplot as plt
import numpy as np

a = int(input('Wprowadz wartosc dla liczby a: '))
b = int(input('Wprowadz wartosc dla liczby b: '))
c = int(input('Wprowadz wartosc dla liczby c: '))
listRange = int(input('Provide a value for list range: '))

def figA():

    x = np.linspace(-1, 10, 100)
    y = a*x+b
    
    plt.plot(x, y, color = 'blue', label = 'Linear function a*x+b')
    plt.title('Linear function a*x+b')
    plt.xlabel('x', color = 'magenta')
    plt.ylabel('y', color = 'black')
    plt.legend(loc = 'lower right')
    plt.grid()


def figB():
    
    x = np.linspace(-2, 2, 5)
    y = a*x**2+b*x+c
    
    fig,ax = plt.subplots()
    
    ax.plot(x, y)
    plt.show()
    
    
  
def figC():
    
    xValue = list(range(-listRange,listRange))
    if 0 in xValue: xValue.remove(0)
    equation = [2/(x**2) for x in xValue]
     
    plt.grid()
    plt.ylim(0,max(equation))
    plt.plot(xValue, equation)

    
    
def main():
    
    figA()
    figB()
    figC()
    
    plt.show()
    
if __name__ == '__main__':
    main()