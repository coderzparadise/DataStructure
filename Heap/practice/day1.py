# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 18:03:36 2021

@author: coderzparadise

Fastest time to complete and explain: 19 minutes
"""
import heapq

class Heap(object):
    def __init__(self):
        self.item = []
        
    # parent 1 can have two childs: 3,4
    def parent(self, index):
        if index == 0:
            return 0
        return ( index - 1 ) // 2
    
    # parent node 2 has two children: 5,6
    def left_child(self, index):
        if index >= len(self.item):
            return -1
        
        result = ( index * 2 ) + 1
        if result >= len(self.item):
            return -1
        return result
    
    def right_child(self, index):
        if index >= len(self.item):
            return -1
        
        result = ( index * 2 ) + 2
        
        if result >= len(self.item):
            return -1
        return result
        
        
    def insert(self, new_item):
        self.item.append(new_item)
        index = len(self.item) - 1
        
        #                        MAX HEAP
        while index > 0 and new_item > self.item[self.parent(index) ]:
            self.item[index] = self.item[self.parent(index) ]
            index = self.parent(index)
        
        self.item[index] = new_item
    
    def display(self):
        for i in self.item:
            print( i, end=' ')
        print()
        
        
    
if __name__ == "__main__":
    print('start\n')
    h = Heap()
    
    h.insert(39)
    h.insert(40)
    h.insert(12)
    h.insert(20)
    h.insert(50)
    h.insert(8)
    h.insert(17)
    
    h.display()
    
    print(h.right_child(2) )
    
    print()
    
    

    
    ### practice importing python heap and using heapq library
    # h2 = []
    # heapq.heappush(h2, 12)
    # heapq.heappush(h2, 25)
    # heapq.heappush(h2, 39)
    # heapq.heappush(h2, 9)
    # heapq.heappush(h2, 30)
    # print(h2)
    # heapq.heappop(h2)
    # print(h2)
    # heapq.heappushpop(h2, 45)
    # print(h2)
    # heapq.heapreplace(h2, 77)
    # print(h2)
    # print( heapq.nsmallest(2, h2) )
    # print( heapq.nlargest(3, h2))
            
        
    
    