# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 15:34:21 2021

@author: coderzparadise

Fastest time to implement code and explain Data Structure: Binary Search Tree (BST)
    -15 minutes
"""
from BST import BST

if __name__ == "__main__":
    print('start program')
    b = BST()
    b.insert(44)
    b.insert(57)
    b.insert(20)
    b.insert(25)
    b.insert(49)
    b.insert(21)
    b.insert(61)
    b.insert(100)
    b.display('')
    print('\n')
    
    print( b.sum_at_depth(6) )
    print( b.find_depth_of_item(58) )
    print(b.height() )
    print(b.smallest() )
    print(b.largest() )
    print(b.find(100) )
    print('\n')
    print(b.print_at_depth(4
                           ) )
    print( b.sum_of_nodes() )
    print( b.num_of_nodes() )
    
    bst_list = []
    b.extract_to_list(bst_list)
    print(bst_list)
    print('\n')
    
    ##############
    
    ages = [9,14,17,21, 22, 37, 40, 50]
    b2 = BST.build_BST(None, ages)
    b2.display('')
