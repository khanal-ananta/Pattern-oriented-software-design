#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 23:59:34 2020

@author: ananta
"""

# ITarget class
from abc import ABC,abstractmethod

class Laptop(ABC):
    @abstractmethod
    def connectA(self):
        pass

class Mouse():
    def connectB(self):
        print("sending singnal from mouse to adapter")
 
 
class Adapter(Laptop):
    
        
    def connectA(self):
        m1 = Mouse()
        m1.connectB() # calling with self is most important
        print("singnal converted")
        print("sending converted signal to laptop")
    
def main():        
    class Client():
    
        adapter = Adapter()
        adapter.connectA()
        print("laptop got the signal")
            
if __name__ == "__main__" :
    main()
               