# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:46:43 2020

@author: Hugo
"""

#Projekt 4 

class Matrix():

    def __init__(self, height, width):
        self.rows = [[0]*width for i in range(height)]
        self.height = height
        self.width = width

    def __str__(self):
        s = "\n" + "\n".join([str(i) for i in [rows for rows in self.rows] ]) + "\n"
        return s

    def __repr__(self):
        return (f'{self.__class__.__name__} ({self.height!r} , {self.width!r})')

    def len(self):
        return self.height * self.width

    def __add__(self, matrix2):
        return

    def __mul__(self, matrix2):
        return

    def remove(self, item):
        return

    def fill_matrix(self, fill_list):
        index = 0
        for i in range(len(self.rows)):
            try:
                for j in range(len(self.rows[i])):
                    self.rows[i][j] = fill_list[index]
                    index += 1
            except IndexError:
                print (f"Matrix not filled \nMatrix fill stopped at: row {i}, Column {j}")
                break    
            