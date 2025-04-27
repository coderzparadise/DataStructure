# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 19:02:54 2021

@author: coderzparadise
"""

class HashMap(object):
    def __init__(self, size):
        self.num_of_buckets = size
        self.num_of_items = 0
        self.item = []
        for i in range(size):
            self.item.append( [] )
    
    def get_hash_func(self, new_item):
        result = 0
        for c in new_item:
            result += ord(c)
        return result % self.num_of_buckets

    # overloading add() and insert() function for easy-use
    def add(self, new_item):
        if self.num_of_items / self.num_of_buckets > 1:
            # print('hereee')
            new_hashmap = self.insert_full(new_item)
            self.__dict__ = new_hashmap.__dict__
            
        else:
            index = self.get_hash_func(new_item)
            self.item[index].append(new_item)
            self.num_of_items += 1

    # overloading insert() and add() function for easy-use
    def insert(self, new_item):
        if self.num_of_items / self.num_of_buckets > 1:
            # print('hereee')
            new_hashmap = self.insert_full(new_item)
            self.__dict__ = new_hashmap.__dict__
            
        else:
            index = self.get_hash_func(new_item)
            self.item[index].append(new_item)
            self.num_of_items += 1
            
    def insert_full(self, new_item):
        result = HashMap( (self.num_of_buckets * 2) + 1)
        for i in range(len(self.item) ):
            for j in range(len(self.item[i]) ):
                result.insert(self.item[i][j] )
        result.insert(new_item)
        return result
    
    def display(self):
        print(self.item)
            
    
        