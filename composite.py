#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 23:17:39 2020

@author: ananta
"""

from abc import ABC,abstractmethod


class Component(ABC):
    @abstractmethod
    def salary(self):
        pass
    
    
class Composite(Component):
        
    def __init__(self,sal):
        self.sal = sal
        self.child_component = []
        
          
    
    def add_component(self,comp):
        self.child_component.append(comp)
        
        
    def remove_component(self,comp):
        self.child_component.remove(comp)
        
       
    def salary(self):
        print(self.sal)
        for comp in self.child_component:
            print("\t", end ="") 
            comp.salary()
            

class Leaf(Component):
    def __init__(self,sal):
        self.sal = sal
        
    def salary(self):
        print("\t", end ="") 
        print(self.sal)
        
    
class client():
    ananta = Leaf(100)
    binod = Leaf(200)
    rita = Leaf(300)
    sita = Leaf(400)
       
    dev_team_lead = Composite(5000)
    qa_team_lead = Composite(4000)
    ceo = Composite(100000)
    
    ceo.add_component(dev_team_lead)
    ceo.add_component(qa_team_lead)
    
    dev_team_lead.add_component(ananta)
    dev_team_lead.add_component(binod)
    
    qa_team_lead.add_component(rita)
    qa_team_lead.add_component(sita)
    
    print('salary of object under ceo')
    ceo.salary()
    print('salary of object under developer team')
    dev_team_lead.salary()
    print('salary of object under qa team')
    qa_team_lead.salary()   
    print('leaf object salary')
    ananta.salary()
    binod.salary()
    rita.salary()
    sita.salary()
    
    
    
    
    
    
    
    
    
       
        
    