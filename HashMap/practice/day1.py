# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 18:41:35 2021

@author: coderzparadise

Fastest time to complete and explain: 23 minutes
"""

class HashMap(object):
    def __init__(self, size):
        self.item = []
        self.num_of_items = 0
        self.num_of_buckets = size
        for i in range(size):
            self.item.append( [] )
    
    def insert(self, new_item):
        if self.num_of_items / self.num_of_buckets > 1:
            new_hashmap = self.insert_full(new_item)
            self.__dict__ = new_hashmap.__dict__
            
        else:
            bucket = self.get_hash(new_item)
            self.item[bucket].append(new_item)
            self.num_of_items += 1
            
    def insert_full(self, new_item):
        new_size = (self.num_of_buckets * 2) + 1
        h = HashMap(new_size)
        for i in range( len(self.item) ):
            for j in range( len(self.item[i]) ):
                h.insert(self.item[i][j] )
        h.insert(new_item)
        return h
        
    
    def get_hash(self, word):
        result = 0
        for c in word:
            result += ord(c)
        
        return result % self.num_of_buckets
    
    def display(self):
        for i in range(len(self.item) ):
            for j in self.item[i]:
                print( j, end = ' ')
            print()
        print()
    
    
    

if __name__ == "__main__":
    print('start\n')
    h = HashMap(2)
    h.insert('soccer')
    h.insert('pizza')
    h.insert('basketball')
    h.insert('rocket')
    h.insert('base')
    h.display()
    
    
    # d = dict()
    # d.update( {'soccer': 2})
    # print(d)
    # d['base'] = 5
    # d['basket'] = 12
    # d.pop('base')
    # d['base'] = 10
    # print(d)
    # d['base'] = d['base'] + 1
    # print( d )
    # d['base'] += 1
    # print(d)
    # del d['base']
    # print(d)
    # d.update( {'base':10} )
    # print( d )
    
    # for k in d.keys():
    #     print(k)
    # print()
    
    # for v in d.values():
    #     print(v)
    # print()
    
    # for k,v in d.items():
    #     print( k, v)
        
    # ############################
    
    # name = ['a', 'd', 'c', 'r', 'p', 'j']
    # age = [10, 20, 30, 40, 50, 60]
    
    # z = { k:v for k,v in zip(name, age) }
    # print(z)