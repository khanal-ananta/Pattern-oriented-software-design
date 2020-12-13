#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:22:32 2020

@author: ananta
"""

from abc import ABC,abstractmethod

# command interface
class Command():
    @abstractmethod
    def execute():
        pass
    
    
# receiver    
class WordDocument():
    def open_file(self):
        print('word document is open')
        
    def close_file(self):
        print('word document is close')
        
        
# command interface implementation
class OpenCommand(Command):
    def __init__(self,w1):
        self.w1 = w1
    
    def execute(self):
        self.w1.open_file()
        
class CloseCommand(Command):
    def __init__(self,w2):
        self.w2 = w2
        
    def execute(self):
        self.w2.close_file()


# invoker        
class MenuOption():
    def __init__(self,o_file,c_file):
        self.o_file = o_file
        self.c_file = c_file
        
    
    def open_click(self):
        self.o_file.execute()
        
        
    def close_click(self):
        self.c_file.execute()


#client        
class client():
    wd1 = WordDocument()
    o1 = OpenCommand(wd1)
    c1 = CloseCommand(wd1)
    
    m1 = MenuOption(o1,c1)
    
    
    m1.open_click()
    m1.close_click()
    
    
      
        
    