# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 17:49:19 2021

@author: coderzparadise


Fastest time to complete and explain: 13 minutes
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
    
    def display(self):
        if self.is_empty():
            return
        iter_node = self.head
        while iter_node:
            print(iter_node.get_item(), end = ' ' )
            iter_node = iter_node.get_next()
        print()
        
    def pop(self):
        if self.is_empty():
            return
        
        old_head = self.head
        self.head = self.head.get_next()
        return old_head.get_item()
    
    def peak(self):
        if self.is_empty():
            return
        return self.head.get_item()
    
    
if __name__ == "__main__":
    print('start\n')
    
    q = Queue()
    q.insert(20)
    q.insert(80)
    q.insert(30)
    q.insert(45)
    q.insert(2)
    q.display()
    
    

    # q2 = []
    # q2.append(0)
    # q2.append(1)
    # q2.append(2)
    # q2.append(3)
    # q2.append(4)
    # q2.append(5)
    # print()
    # print( q2.pop(0) )
    # for i in range(len(q2) ):
    #     print(q2[i], end = ' ')
        
    
            
            
            
            