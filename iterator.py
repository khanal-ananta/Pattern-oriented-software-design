#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 01:36:15 2020

@author: ananta
"""

from abc import ABC,abstractmethod


# a = np.array([1,2,3,4])

# len(a)   #answer = 4

# list(a).index(a[-1])
# answer is 3
# this is to print the values
# print(a)
# print(a[1])

# a=1
# print(a)
# a+=1
# print(a)

# iterator class

class Iterator(ABC):
    @abstractmethod
    def has_next():
        pass
    @abstractmethod
    def next_obj():
        pass
    
    #container class   

class Container(ABC):
    @abstractmethod
    def create_iterator():
        pass
    
# implement container class    
class ConcreteContainer(Container):
    global a_obj
    a_obj=["first","second","third",100]
    
    
    def create_iterator(self):
        i1 = ConcreteIterator()
        return i1

        
#implement iterator class

class ConcreteIterator(Iterator):
    
    def has_next(self):
        
        if ind<len(a_obj):
            return True
        else:
            return False
        
    def next_obj(self):
        
        if self.has_next():
            return a_obj[ind]
            
        
        
        
class Client():
    c1 = ConcreteContainer()
    i2 = c1. create_iterator()
    
    global ind 
    ind = 0
    
    while i2.has_next():
        
        print(i2.next_obj())
        ind+=1
        
           
  
