# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 17:44:47 2021

@author: coderzparadise

Fastest time to implement code and explain Data Structure: Queue
    -10 minutes
"""

from Queue import Queue

if __name__ == "__main__":
    print('start program\n')
    
    q = Queue()
    
    q.insert(2)
    q.insert(5)
    q.insert(8)
    q.insert(13)
    
    q.display()
    
    print( q.pop() )
    q.pop()
    
    q.display()
    
    q.insert(24)
    
    q.display()
    
    print(q.peak())
    
    
    # ### Use python list as a queue (Good for tech interview)
    # print('\n')
    # q2 = []
    
    # q2.append(35)
    # q2.append(88)
    # q2.append(20)
    # q2.append(18)
    # q2.append(17)
    
    # print(q2)
    
    # q2.pop(0) #Remove from position '0' in python list to be considered a queue 
    
    # print( q2)
    
    # for i in range(len(q2)):
    #     print(q2[i], end = ' ')
