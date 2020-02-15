# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 02:41:33 2020

@author: Hugo
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import scipy.stats as stats
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

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
    
    


z = ls1.values.reshape(-1,1)
y = ls2
z_train, z_test, y_train, y_test = train_test_split(z, y, test_size=0.3, random_state=0)

regressor = LinearRegression()
regressor.fit(z_train, y_train)

y_pred = regressor.predict(z_test)

print(regressor.intercept_)
print(regressor.coef_)