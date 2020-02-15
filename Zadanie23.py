# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 21:25:56 2020

@author: Hugo
"""

import collections as coll

list = []

def mediana(n):

    n = int(input('enter the list size: '))
    
    for i in range(0, n):
        print('Enter the number at location',  i+1 ,':')
        item = float(input())
        list.append(item)
    
    
    coll.Counter(list).most_common(1)
    
    return(coll.Counter(list).most_common(1))

print(mediana(list))
