# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:34:11 2021

@author: coderzparadise

Fastest time to implement code and explain Data Structure: Heap
    -8 minutes
"""
from Heap import Heap

import heapq # import/use python library (Good for tech interview)

if __name__ == "__main__":
    print('start program\n')
    
    # Example how to use data strucutre: Heap
    h = Heap()
    
    h.insert(21)
    h.insert(5)
    h.insert(16)
    h.insert(37)
    h.insert(28)
    h.insert(49)
    
    h.display()
    
    print('\nend')
    
    ###################################
    # ## Use heapq from python library (Good for tech interview)
    # hq = []
    # heapq.heappush(hq, -21)
    # heapq.heappush(hq, -5)
    # heapq.heappop(hq)
    
    # heapq.heappush(hq, -16)
    # heapq.heappush(hq, -37)
    # heapq.heappush(hq, -28)
    # heapq.heappush(hq, -49)
    
    # # heapq.heappushpop(hq, -50)  # Push item then pop (2 steps in 1)
    # # heapq.heapreplace(hq, -51)  # Pop then push item (2 steps in 1)
    # print(hq)
    
    # print(heapq.nlargest(4, hq) )  # gets the 'nth' 4 largest items from heapq
    # print(heapq.nsmallest(2, hq) )  # gets the 'nth' 2 largest items from heapq
