#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 19:35:19 2020

@author: ananta
"""

class Singleton:
    __instance = None
    
    def __init__(self):
        
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            print("This class is a singleton!")
        else:
            Singleton.__instance = self
   
    @staticmethod 
    def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
          return Singleton()
      else:
          return Singleton.__instance
          
          
      
         
#s1 = Singleton()
#print (s1)

s2= Singleton.getInstance()
print(s2) 

s3 = Singleton.getInstance()
print(s3)
