# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 19:08:41 2021

@author: coderzparadise

Fastest time to complete and explain: 25 minutes
"""

import numpy as np

class DSF(object):
    def __init__(self, size):
        self.item = np.zeros(size, dtype=int) - 1
    
    def find_root(self, index):
        if self.item[index] < 0:
            return index
        return self.find_root(self.item[index] )
    
    def union(self, index1, index2):
        r1 = self.find_root(index1)
        r2 = self.find_root(index2)
        if r1 != r2:
            if self.item[r1] > self.item[r2]:
                self.item[r2] += self.item[r1]
                self.item[r1] = r2
            else:
                self.item[r1] += self.item[r2]
                self.item[r2] = r1
                
    def display(self):
        print(self.item)
        
    def check_same_set(self, index1, index2):
        r1 = self.find_root(index1)
        r2 = self.find_root(index2)
        return r1 == r2
    
    def num_of_sets(self):
        result = 0
        for i in self.item:
            if i < 0:
                result += 1
        return result
        

if __name__ == "__main__":
    print('start\n')
    d = DSF(10)
    d.union(0, 4)
    d.union(7, 9)
    d.union(4, 7)
    d.display()
    print( d.check_same_set(0, 7))
    print(d.num_of_sets() )