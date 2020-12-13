#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 21:31:18 2020

@author: ananta

"""
# class A():
    
#     def update(self,obs):
#         user = []
#         user.append(obs)
#         return user
        
# class B():
#     a1 = A()
#     b = a1.update('ananta')
#     print(b)


from abc import ABC,abstractmethod


# subject class abstract class
class Subject(ABC):
    @abstractmethod
    def attach(self):
        pass
    
    @abstractmethod
    def detach(self):
        pass
    
    @abstractmethod
    def notify(self):
        pass
    
# object abstract class
class Observer(ABC):
    @abstractmethod
    def update(self):
        pass
    
    
# concreate subject class
class StepStone(Subject):
    global user,jobs
    user = []
    jobs = []
    
    #def __init__(self,*args):
    #    self.o = None
        
    
    def attach(self,obs):  
        user.append(obs)
        
        
    def detach(self,obs):
        user.remove(user,obs)
        
    
            
    def add_job(self,job):
        
        jobs.append(job)
        print(job+" added")
        self.notify()
        
    def notify(self):
        for o in user:
            o.update()   

#concrete observer class            
class JobSeeker(Observer):
    def __init__(self,name):
        self.name = name
    
    def update(self):
        print(self.name+" got notified")
        
        
 # client class       
class Client():
    ss = StepStone()
    
    ss.attach(JobSeeker('ananta'))
    ss.attach(JobSeeker('khanal'))
    
    ss.add_job('google job')
    ss.add_job('ibm job')    
    
    