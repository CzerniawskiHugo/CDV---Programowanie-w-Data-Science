# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:20:01 2020

@author: Hugo
"""

print('Zadanie nr13: Obliczyc n po k Newtona iteracyjnie i rekurencyjnie')



def factorial(n):
    res = 1
    for i in range(res, n + 1):
        res = res * i
    return res

def newt(n, k):
    return factorial(n)/ (factorial(k) * factorial(n - k))

def main():
    n = int(input('Please provide argument n : '))
    k = int(input('Please provide argument k : '))

    print(newt(n, k))

if __name__ == '__main__':
    main()

