# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 17:30:11 2021

@author: coderzparadise

Fastest time to complete and explain: 17 minutes
"""

class Set(object):
    def __init__(self):
        self.item = []
    
    def insert(self, new_item):
        for i in self.item:
            if i == new_item:
                return
        self.item.append(new_item)
    
    def display(self):
        print(self.item)
        
    def delete(self, key):
        for i in range(len(self.item)):
            if self.item[i] == key:
                self.item.pop(i)
                return
        


if __name__ == "__main__":
    print('start\n')
    
    s = Set()
    s.insert(20)
    s.insert(12)
    s.insert(99)
    s.insert(55)
    s.insert(12)
    s.insert(40)
    s.insert(44)
    s.insert(55)
    s.display()
    s.delete(12)
    s.display()
    
    
    ## Using python library set() - good for tech interview use
    # s2 = set()
    # s2.add(45)
    # s2.add(99)
    # s2.add(71)
    # print(s2)
    
    # s2.remove(45)
    # print(s2)
    
    
    
    
        
        