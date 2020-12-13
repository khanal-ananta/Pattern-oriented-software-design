#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 14:38:47 2020

@author: ananta
"""
from abc import ABC, abstractmethod

# strategy inteface
class PayMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    
# first strategy implementaion    
class PayPal(PayMethod):
    def pay(self, amount):
        print('you paid {} by paypal'.format(amount))
        
#second   strategy implementaion     
class CreditCard(PayMethod):
    def pay(self, amount):
        print('you paid {} by creditcard'.format(amount))
        
# context which will decide which pay method to use       
class PayMethodContext():
    def __init__(self,pay_m):
        self.pay_m = pay_m
        
    
    def find_pay(self, a):
        self.pay_m.pay(a)
        
# client
class Client():
    pmc1 = PayMethodContext(CreditCard())
    pmc1.find_pay(100)
    
    pmc2 = PayMethodContext(PayPal())
    pmc2.find_pay(200)
    
    
    
    
    
    
    
    
     
        
        
        
        
        
        
    
