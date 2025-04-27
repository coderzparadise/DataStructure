# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 19:21:34 2021

@author: coderzparadise
"""

class Set(object):
    def __init__(self):
        self.item = []

    # overloading insert() and add() function for easy-use
    def insert(self, new_item):
        for i in self.item:
            if i == new_item:
                return
        self.item.append(new_item)
        
    # overloading add() and insert() function for easy-use
    def add(self, new_item):
        for i in self.item:
            if i == new_item:
                return
        self.item.append(new_item)

    # overloading pop() and delete() function for easy-use
    def pop(self, key_item):
        for i in self.item:
            if i == key_item:
                self.item.remove(key_item)

    # overloading delete() and pop() function for easy-use
    def delete(self, key_item):
        for i in self.item:
            if i == key_item:
                self.item.remove(key_item)
        
    def display(self):
        if self == None:
            return
        print(self.item)
        print()
                
    