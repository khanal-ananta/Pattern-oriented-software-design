#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 01:35:57 2020

@author: ananta
"""

from abc import ABC,abstractmethod

# abstract product a
class Shape(ABC):
    @abstractmethod
    def draw():
        pass
    
#concrete product a1   
class  Circle(Shape):
    
    def draw(self):
        print('circle is drawn')
        
# concrete product a2        
class Triangle(Shape):
    def draw(self):
        print('tringle is drawn')
 
    


# abstract product b         
class Color(ABC):
    @abstractmethod
    def fill(self):
        pass
# concrete product b1   
class Red(Color):
    def fill(self):
        print('red color is fill')
 
        
# concrete product b2        
class Blue(Color):
    def fill(self):
        print('blue color is fill')
        
        
class ColorShapeFactory(ABC):
    @abstractmethod
    def get_shape(self,shape):
        pass
    
    @abstractmethod
    def get_color(self,color):
        pass
    

class ConcreteShapeFactory(ColorShapeFactory):
    def get_shape(self,shape_name):
        if shape_name == 'circle':
            return Circle()
        elif shape_name == 'triangle':
            return Triangle()
        else:
            return 
        
    def get_color(self,color_name):
        pass
    
        
class ConcreteColorFactory(ColorShapeFactory):
    
    def get_color(self,color_name):
        
        if color_name == 'red':
            return Red()
        elif color_name == 'blue':
            return Blue()
        else:
            return 
    
    def get_shape(self,shape_name):
        pass
        
        
       
class FactoryProducer():
    
    def get_factory(self,factory_name):
        
        if factory_name == 'shape':
            return ConcreteShapeFactory()
        elif factory_name == 'color':
            return ConcreteColorFactory()
        else:
            return 
        
class Client():
    fp = FactoryProducer()
    
    f1 = fp.get_factory('shape')
    
    shape1 = f1.get_shape('circle')
    shape1.draw()
    shape2 = f1.get_shape('triangle')
    shape2.draw()
    
    
    
    f2 = fp.get_factory('color')
    
    color1 = f2.get_color('red')
    color1.fill()
    color2 = f2.get_color('blue')
    color2.fill()
    
    
        
        
    
                
        