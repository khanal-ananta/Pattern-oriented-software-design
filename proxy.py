#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 11:59:07 2020

@author: ananta
"""

from abc import ABC,abstractmethod

class College(ABC):
    @abstractmethod
    def studying_in_college():
        pass
    
    
class RealCollege(College):
    def studying_in_college(self):
        print("studying in clz\n")
        
class CollegeProxy(College):
    def __init__(self):
        self.fee_balance =1000
        self.college = None
        
    def studying_in_college(self):
        print("proxy in action. checking if the balance of student is clear or not")
        
        if self.fee_balance >= 500:
            self.college = RealCollege()
            self.college.studying_in_college()
            
        else:
            print("your fee is less than 500 first pay the fee\n")
            

def main():
            
    class Client():
        proxycollege = CollegeProxy()
    
        # trying with default balance
        proxycollege.studying_in_college()
    
        proxycollege.fee_balance = 400
    
        proxycollege.studying_in_college()
    
    
if __name__ == "__main__":
    main()
           
        
    


