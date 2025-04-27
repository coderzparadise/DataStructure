# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 13:15:49 2021

@author: coderzparadise

Fastest time to complete and explain: 12 minutes
"""

import heapq

class Heap(object):
    def __init__(self):
        self.item = []
    
    def parent(self, index):
        return (index - 1) // 2
    
    def insert(self, new_item):
        self.item.append(new_item)
        index = len(self.item) - 1
        
        while index > 0 and new_item < self.item[ self.parent(index) ]:
            self.item[index] = self.item[ self.parent(index) ]
            index = self.parent(index)
        
        self.item[index] = new_item
    
    def display(self):
        print(self.item)


if __name__ == "__main__":
    print('start\n')
    
    h = Heap()
    h.insert(100)
    h.insert(80)
    h.insert(20)
    h.insert(50)
    h.insert(3)
    h.insert(24)
    h.display()
            
    
    # h2 = []
    # heapq.heappush(h2, 10)
    # heapq.heappush(h2, 30)
    # heapq.heappush(h2, 55)
    # heapq.heappush(h2, 9)
    # heapq.heappush(h2, 11)
    # print(h2)
    # heapq.heappop(h2)
    # print(h2)
    # heapq.heappush(h2, 77)
    # print(h2)
    # print( heapq.nlargest(2, h2))