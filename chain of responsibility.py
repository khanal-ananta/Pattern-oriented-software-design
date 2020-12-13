#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 17:06:28 2020

@author: ananta
"""

from abc import ABC,abstractmethod

class Employee(ABC):
    def next_supervisor(self,supervsr1):
        self.supervsr = supervsr1
        
    @abstractmethod   
    def apply_leave(self,name,day):
        pass
    
class TeamLeader(Employee):
          
    def apply_leave(self,name,day):
        max_days=10
        if day < max_days:           
            print('granted {} days leave for {}'.format(day,name))
        else:
            self.supervsr.apply_leave(name,day)
            
class HR(Employee):
           
    def apply_leave(self,name,day):
        max_days=30
        if day <max_days:
            print('granted {} days leave for {}'.format(day,name))
        else:
            print('please meet HR personally')
            
class client():
    tl = TeamLeader()
    hr = HR()
    tl.next_supervisor(hr)
    
    tl.apply_leave('ananta',5)
    tl.apply_leave('elin',20)
    tl.apply_leave('kamal',35)
            
            
            
    
    