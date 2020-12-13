#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:54:54 2020

@author: ananta
"""

from abc import ABC,abstractmethod

# product interface
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass
#factory interface
class ShapeFactory(ABC):
    @abstractmethod
    def get_shape(self,shape_name):
        pass
    
# concreate product 1    
class Circle(Shape):
    def draw(self):
        print('circle is drawn')
        
 # concrete product 2   
class Triangle(Shape):
    def draw(self):
        print('triangle is drawn')
        
 
# concreate facory
class ConcreateShapeFactory(ShapeFactory):
    
    
    def get_shape(self,shape_name):
        
        # there is no self.shape_name ==circle 
        if shape_name == 'circle':
            return Circle()
        elif shape_name == 'triangle':
            return Triangle()
        else:
            return 
        
# client class
class client():
    csf1 = ConcreateShapeFactory()
    
    shape1 = csf1.get_shape('circle')
    shape1.draw()
    
    shape2 = csf1.get_shape('triangle')
    shape2.draw()
    
    
    
    
    
        
         
        
    
       
        
        
        
       
        
        
    
