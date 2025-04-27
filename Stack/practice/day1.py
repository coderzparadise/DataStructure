# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 14:25:27 2021

@author: coderzparadise

Fastest time to complete and explain: 42 minutes
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
        popped = self.head.get_item()
        self.head = self.head.get_next()
        return popped
    
    def display(self):
        if self.is_empty():
            return
        iter_node = self.head
        while iter_node:
            print(iter_node.get_item(), end = ' ' )
            iter_node = iter_node.get_next()
        print()
    
    def peak(self):
        if self.is_empty():
            return
        return self.head.get_item()



if __name__ == "__main__":
    print('start\n')
    
    # custom stack
    s = Stack()
    s.insert(32)
    s.insert(44)
    s.insert(72)
    
    s.display()
    print( s.peak() )
    print('\n')
    
    
    # list stack
    st = []
    st.append(23)
    st.append(99)
    st.append(20)
    st.append(50)
    st.pop()
    st.append(51)
    print(st)
    
    for i in range(len(st)-1, -1, -1 ):
        print(st[i])
        
    