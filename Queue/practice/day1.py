# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 13:06:14 2021

@author: coderzparadise


Fastest time to complete and explain: 17 minutes
"""

class Node(object):
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
        
    def get_item(self):
        return self.item
    
    def get_next(self):
        return self.next
    
    
class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def is_empty(self):
        return self.head == None
    
    def insert(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
            self.tail = self.head
        else:
            self.tail.next = Node(new_item)
            self.tail = self.tail.get_next()
            
    def pop(self):
        if self.is_empty():
            return
        popped = self.head.get_item()
        self.head = self.head.get_next()
        return popped
    
    def display(self):
        if self.is_empty():
            return
        iter_node = self.head
        while iter_node:
            print(iter_node.get_item(), end = ' ')
            iter_node = iter_node.get_next()
        print()
        
    def peak(self):
        if self.is_empty():
            return
        return self.head.get_item()
    

if __name__ == "__main__":
    print('start\n')
    q = Queue()
    q.insert(10)
    q.insert(20)
    q.insert(30)
    q.insert(40)
    q.display()
    print( q.pop() )
    q.display()
    q.insert(66)
    q.display()
    
    p = []
    p.append(0)
    p.append(1)
    p.append(2)
    p.append(3)
    p.append(4)
    p.append(5)
    print(p)
    p.pop(0)
    print(p)
    print(p.index(4) )
    
    