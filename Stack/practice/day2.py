# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 14:57:36 2021

@author: coderzparadise

Fastest time to complete and explain: 26 minutes
"""

class Node(object):
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
        
    def get_item(self):
        return self.item
    
    def get_next(self):
        return self.next
    

class Stack(object):
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def insert(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
        else:
            old_head = self.head
            insertee = Node(new_item, old_head)
            self.head = insertee
            
    def pop(self):
        if self.is_empty():
            return
        
        old_head = self.head
        self.head = self.head.get_next()
        return old_head.get_item()
    
    def display(self):
        if self.is_empty():
            return
        iter_node = self.head
        while iter_node:
            print(iter_node, end=' ')
            iter_node = iter_node.get_next()
        print()
        
    def peak(self):
        if self.is_empty():
            return
        return self.head.get_next()
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        