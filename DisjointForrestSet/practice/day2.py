# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 12:31:55 2021

@author: coderzparadise

Fastest time to complete and explain: 14 minutes
"""
import numpy as np

class DSF(object):
    def __init__(self, size):
        self.item = np.zeros(size, dtype=int)-1
    
    def root(self, index):
        if self.item[index] < 0:
            return index
        return self.root(self.item[index] )
    
    def union(self, index1, index2):
        r1 = self.root(index1)
        r2 = self.root(index2)
        
        if r1 != r2:
            if self.item[r1] < self.item[r2]:
                self.item[r1] += self.item[r2]
                self.item[r2] = r1
            else:
                self.item[r2] += self.item[r1]
                self.item[r1] = r2
                
    def num_of_sets(self):
        counter = 0
        for i in self.item:
            if i < 0:
                counter += 1
        return counter
    
    def check_same_set(self, index1, index2):
        r1 = self.root(index1)
        r2 = self.root(index2)
        return r1 == r2
    
    def display(self):
        print(self.item)
        
    
            
            
        
    
    
    
    