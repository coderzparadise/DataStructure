# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:47:57 2021

@author: coderzparadise

Fastest time to complete and explain: 23 minutes
"""

class HashMap(object):
    def __init__(self, size):
        self.item = []
        self.num_of_items = 0
        self.bucket_size = size
        for i in range(size):
            self.item.append( [] )
    
    def display(self):
        for i in range(len(self.item) ):
            for j in range(len(self.item[i]) ):
                print(self.item[i][j], end=' ')
            print()
    
    def insert(self, new_item):
        if (self.num_of_items / self.bucket_size ) > 1:
            new_hash = self.insert_full(new_item)
            self.__dict__ = new_hash.__dict__
            
        else:
            index = self.get_hash(new_item)
            self.item[index].append(new_item)
            self.num_of_items += 1
    
    def insert_full(self, new_item):
        new_size = (self.bucket_size*2)+1
        h = HashMap(new_size)
        
        for i in range(len(self.item)):
            for j in range(len(self.item[i])):
                h.insert(self.item[i][j] )
        
        h.insert(new_item)
        return h
    
    def get_hash(self, word):
        res = 0
        for c in word:
            res += ord(c)
        return res % self.bucket_size


if __name__ == "__main__":
    print('start\n')
    h = HashMap(2)
    h.insert("soccer")
    h.insert('laptop')
    h.insert('tv')
    h.insert('music')
    h.display()
    print('\n')
    
    ####################
    
    h1 = dict()
    h1['soccer'] = 11
    h1['hockey'] = 6
    h1.update( {"football":15} )
    # del h1['soccer']
    h1.pop('soccer')
    h1['basketball'] = 5
    print(h1)
    
    n1 = [0,1,2,3,4,5]
    a2 = ['a', 'b', 'c', 'd', 'e', 'f']
    
    z = {k:v for k,v in zip(n1,a2)}
    print(z)
    
    for k,v in z.items():
        print(k,v)