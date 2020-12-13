#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:29:02 2020

@author: ananta
"""

from abc import ABC, abstractmethod


# it inherite abstract class ABC
class Room(ABC):
    @abstractmethod
    def show_room(self):
        pass


# concreate component
class SimpleRoom(Room):
    def show_room(self):
        return 'normal room +'


# decorator class   
class RoomDecorator(Room):
    def __init__(self, special_room):
        self.special_room = special_room
    # in python we can avoid below code    
    @abstractmethod
    def show_room(self):
        pass
        #return self.special_room.show_room()


# one concreate decorator        
class ColorDecorator(RoomDecorator):

    def show_room(self):
        return self.special_room.show_room() + self.add_color()

    def add_color(self):
        return ' color added +'


# second concrete decorator   
class CurtainDecorator(RoomDecorator):

    def show_room(self):
        return self.special_room.show_room() + self.add_curtain()

    def add_curtain(self):
        return ' curtain added'


class Client():
    r1 = CurtainDecorator(ColorDecorator(SimpleRoom()))
    print(r1.show_room())
