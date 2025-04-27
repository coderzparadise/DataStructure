# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 15:49:58 2021

@author: coderzparadise
"""
import numpy as np

class DSF(object):
    def __init__(self, size):
        self.item = np.zeros(size, dtype=int)-1
    
    def find_root(self, index):
        if self == None:
            return
        elif self.item[index] < 0:
            return index
        return self.find_root( self.item[index] )
    

    def union_by_size(self, index1, index2):
        if self == None:
            return
        r1 = self.find_root(index1)
        r2 = self.find_root(index2)
        if r1 != r2:
            if self.item[r1] < self.item[r2]:
                # we add to self.item[r1] b/c we need to carry the weight of self.item[r2]
                self.item[r1] += self.item[r2]
                self.item[r2] = r1
            else:
                self.item[r2] += self.item[r1]
                self.item[r1] = r2
                
    def num_of_sets(self):
        result = 0
        for i in self.item:
            if i < 0:
                result += 1
        return result
    
    def check_same_set(self, index1, index2):
        if self == None:
            return
        r1 = self.find_root(index1)
        r2 = self.find_root(index2)
        if r1 != r2:
            return False
        return True
                
    def display(self):
        print(self.item)
        