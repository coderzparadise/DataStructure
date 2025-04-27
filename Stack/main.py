# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 16:24:00 2021

@author: coderzparadise

Fastest time to implement code and explain Data Structure: Stack
    -12 minutes
"""

from Stack import Stack

if __name__ == "__main__":
    
    print('start program\n')
    
    # Example how to use Data Strucutre: Stack()
    s = Stack()
    
    s.insert(4)
    s.insert(7)
    s.insert(9)
    s.insert(13)
    s.insert(17)
    
    s.display()
    
    s.pop() 
    
    s.display()
    
    s.insert(33)
    s.display()
    
    print( s.peak() )
    
    ###############################
    ### Use python list as stack (good for tech interview)
    # q = []
    # q.append(3)
    # q.append(7)
    # q.append(11)
    # q.append(9)
    # q.pop()
    # print(q)
    
    ### Iterate python list in reverse = iterate in reverse is a stack
    # for i in range(len(q)-1, -1, -1 ):
    #     print(q[i])
    
