# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 14:46:52 2021

@author: coderzparadise

Fastest time to complete and explain: 19 minutes
"""

class Set(object):
    def __init__(self):
        self.item = []
    
    
    def insert(self, new_item):
        for i in self.item:
            if new_item == i:
                return
        self.item.append(new_item)
        
    def pop(self, key_item):
        if key_item in self.item:
            index = self.item.index(key_item)
            self.item.pop(index)
    
    def display(self):
        for i in self.item:
            print(i, end = ' ')
        print()


if __name__ == "__main__":
    print('start\n')
    s = Set()
    
    s.insert(20)
    s.insert(99)
    s.insert(77)
    s.insert(70)
    s.insert(33)
    s.insert(6)
    
    s.display()
    
    s.pop(77)
    
    s.display()
    
    
    ############## #Using python set (Good for tech interview)
    # s2 = set()
    # s2.add(55)
    # s2.add(56)
    # s2.add(57)
    # s2.add(58)
    
    # print(s2)
    # s2.remove(55)
    
    # print( s2 )
    
    