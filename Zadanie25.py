# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 01:07:48 2020

@author: Hugo
"""

import sys
import math

ls = []




n = int(input('enter the list size: '))
    
for i in range(0, n):
    print('Enter the number at location',  i+1 ,':')
    item = float(input())
    ls.append(item)
       
       
def main():
    
    avg = sum(ls)/len(ls)
    print("Avg =  %f" % avg)
    for number in sorted(ls):
        print("number = %f, odchylenie od sredniej = %f" %(number,math.fabs(avg-number)))
main()
        
        
        
        
        
        
