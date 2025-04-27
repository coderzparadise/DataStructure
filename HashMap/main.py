# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 19:00:42 2021

@author: coderzparadise

Fastest time to implement code and explain Data Structure: HashMap
    -10 minutes
"""
from HashMap import HashMap


if __name__ == "__main__":
    print('start program\n')
    
    ### Example how to use HashMap() data structure
    h = HashMap(2)
    
    h.insert('soccer')
    h.insert('basketball')
    h.insert('football')
    h.insert('pizza')
    
    h.display()
    
    
    
    ### Using Python library Hashmap (good for tech interviews!)
    
    # #### method 1
    # h2 = dict()
    # h2['soccer'] = 11
    # h2['bball'] = 5
    # h2['hockey'] = 7
    
    # # h2.pop('soccer')
    # # del h2['soccer']
    
    # h2.update({'baseball': 12})
    
    # print(h2)
    
    # for h2_key in h2.keys():
    #     print(h2_key)
        
    # for h2_value in h2.values():
    #     print(h2_value)
        
    
    
    # #### method 2
    # names = ['tupac', 'jcole', 'asap', 'kendrick', '50 cent']
    # ages = [32, 33, 29, 27, 49]
    
    # h3 = {k:v for k,v in zip(names, ages)}
    # for i in h3.items():
    #     print(i)
    # print('\n', h3)



    # ### method 3
    # h10 = {'rocky':1, 'asap':2, 'check':3}
    # print(h10)
    
    

    
    
    
    
