

import math
import operator as op

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return (self.x, self.y)
    
    def __basic_operation(self, vector, operation):
        return (operation(self.x, vector.x), (operation(self.y, vector.y)))
    
    def get_lenght(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def inverse(self):
        self.x = -self.x
        self.y = -self.y
        
        return self
    
    def add(self, vector):
        x, y = self.__basic_operation(self, vector, op.add)
        return Vector2D(x, y)      
    
    def subtract(self, vector):
        x, y = self.__basic_operation(self, vector.inverse(), op.sub)
        return Vector2D(x, y)      
   
    def multiply_by_number(self, number=1):
        x, y = self.__basic_operation(self, Vector2D(number, number), op.mul)
        
    def multiply_scalar(self, vector, ):
        return self.x * vector.x + self.y * vector.y