#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 13:40:35 2020

@author: ananta
"""

# model class
class StudentModel():
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        

    def get_name(self):
        return self.name
    
    def get_rollno(self):
        return self.rollno
    
# view class    
class StudentView():
    def print_details(self,name,rollno):
        print(name,rollno)
        #print('{}{}'.format(self.name,self.rollno))
        

# controller class        
class StudentController():
    def __init__(self,model,view):
        self.model = model
        self.view = view        
    
    def manupulates(self):
        self.view.print_details(self.model.get_name(),self.model.get_rollno())
        
        
# client class       
class MvcPattern():
    model1 = StudentModel("ananta",29)
    view1 = StudentView()
    controller1 = StudentController(model1,view1)
    
    controller1.manupulates()
