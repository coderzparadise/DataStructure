# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 17:33:46 2021

@author: coderzparadise
"""
import numpy as np

class EdgeList(object):
    def __init__(self, nodes):
        self.node = nodes
        self.item = []

    # overloading insert() and add() function for easy-use
    def insert(self, item1, item2):
        if item1 in self.node and item2 in self.node:
            index1 = self.node.index(item1)
            index2 = self.node.index(item2)
            #Append edge1, edge2, weight of edge
            self.item.append([index1, index2, 0])
        else:
            index1 = item1
            index2 = item2
            self.item.append([index1, index2, 0])

    # overloading add() and insert() function for easy-use  
    def add(self, item1, item2):
        if item1 in self.node and item2 in self.node:
            index1 = self.node.index(item1)
            index2 = self.node.index(item2)
            #Append edge1, edge2, weight of edge
            self.item.append([index1, index2, 0])
        else:
            index1 = item1
            index2 = item2
            self.item.append([index1, index2, 0])
        
    def display(self):
        print(self.item)
        
    def edge_list_to_adj_list(self):
        a = []
        for i in range(len(self.node) ):
            a.append([])
        for j in self.item:
            a[j[0]].append( j[1] )
        return a
    
    def edge_list_to_adj_matrix(self):
        result = np.zeros( (len(self.node), len(self.node)), dtype = bool)
        for i in self.item:
            result[i[0]][i[1]] = True
        return result
        