# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 18:56:57 2021

@author: coderzparadise
"""

from Node import Node

class Stack(object):
    def __init__(self):
        self.head = None

    # overloading insert() and add() function for easy-use
    def insert(self, new_item):
        if self.head == None:
            self.head = Node(new_item)
        else:
            old_head = self.head
            self.head = Node(new_item, old_head)

    # overloading add() and insert() function for easy-use
    def add(self, new_item):
        if self.head == None:
            self.head = Node(new_item)
        else:
            old_head = self.head
            self.head = Node(new_item, old_head)
            
            
    def is_empty(self):
        return self.head == None


    # overloading pop() and delete() function for easy-use
    def pop(self):
        if self.head == None:
            return
        pop_item = self.head
        self.head = self.head.get_next()
        return pop_item.get_item()

    # overloading delete() and pop() function for easy-use
    def delete(self):
        if self.head == None:
            return
        pop_item = self.head
        self.head = self.head.get_next()
        return pop_item.get_item()
    
    def display(self):
        if self.head == None:
            return
        iter_node = self.head
        while iter_node != None:
            print(iter_node.get_item(), end=' ' )
            iter_node = iter_node.get_next()
        print()
        
    def peak(self):
        if self.is_empty():
            return
        return self.head.get_item()