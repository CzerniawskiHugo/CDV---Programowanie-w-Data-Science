# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 02:23:54 2020

@author: Hugo
"""
import numpy as np
import statistics as stat
from scipy import stats


ls1 = []
n1 = int(input('enter the list number one size: '))
    
for i in range(0, n1):
    print('Enter the number at location',  i+1 ,':')
    item = float(input())
    ls1.append(item)

ls2 = []
n2 = int(input('enter the list number two size: '))

for i in range(0, n2):
    print('Enter the number at location',  i+1 ,':')
    item = float(input())
    ls2.append(item)
    
print(stats.pearsonr(ls1, ls2))