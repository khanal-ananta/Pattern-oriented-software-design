#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 23:28:30 2020

@author: ananta
"""

from abc import ABC, abstractmethod

# abstract class for all the methods
class HouseTemplate(ABC):
    def build_house(self):
        # first define the emthods
        # these two are two different things        
        self.build_foundation()
        self.build_wall() 
        
    def build_foundation(self):        
            print('foundation is build')
        
    @abstractmethod        
    def build_wall(self):
            pass   
         
class WoodenHouse(HouseTemplate):
    def build_wall(self):
        print('wooden wall is build')
        print('wooden house is build')
        
class GlassHouse(HouseTemplate):
    def build_wall(self):
        print('glass wall is build')
        print('glass house is build')
        
class Client():
    
    wooden_house = WoodenHouse()
    wooden_house.build_house()
    print('....................')
    glass_house = GlassHouse()
    glass_house.build_house()
        
        
    