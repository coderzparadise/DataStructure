# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 23:00:11 2021

@author: coderzparadise
"""

class Heap(object):
    def __init__(self):
        self.item = []
        self.num_of_items = 0
        
    def parent(self, index):
        return (index - 1) // 2
    
    def left_child(self, index):
        result = (index * 2) + 1
        if len(self.item) < result:
            return -1
        return result
    
    def right_child(self, index):
        result = (index * 2) + 2
        if (len(self.item) < result):
            return -1
        return result
    

    # overloading insert() and add() function for easy-use
    def insert(self, new_item):
        self.item.append(new_item)
        index = len(self.item) - 1
        
        while index > 0 and new_item > self.item[ self.parent(index) ]:
            self.item[index] = self.item[ self.parent(index) ]
            index = self.parent(index)
        
        self.item[index] = new_item
        self.num_of_items += 1    

    
    # overloading add() and insert() function for easy-use
    def add(self, new_item):
        self.item.append(new_item)
        index = len(self.item) - 1
        
        while index > 0 and new_item > self.item[ self.parent(index) ]:
            self.item[index] = self.item[ self.parent(index) ]
            index = self.parent(index)
        
        self.item[index] = new_item
        self.num_of_items += 1
            
    def display(self):
        print(self.item)
        
            