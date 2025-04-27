# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 17:59:32 2021

@author: coderzparadise
"""
import numpy as np

class AdjacencyMatrix(object):
    def __init__(self, nodes):
        self.node = nodes
        self.item = np.zeros((len(self.node), len(self.node)), dtype = bool)
        
    # overloading insert() and add() function for easy-use
    def insert(self, item1, item2):
        if item1 in self.node and item2 in self.node:
            index1 = self.node.index(item1)
            index2 = self.node.index(item2)
            self.item[index1][index2] = True
        else:
            index1 = item1
            index2 = item2
            self.item[index1][index2] = True

    # overloading add() and insert() function for easy-use  
    def add(self, item1, item2):
        if item1 in self.node and item2 in self.node:
            index1 = self.node.index(item1)
            index2 = self.node.index(item2)
            self.item[index1][index2] = True
        else:
            index1 = item1
            index2 = item2
            self.item[index1][index2] = True
            
    def display(self):
        print(self.item)
            
    def adj_matrix_to_adj_list(self):
        a = []
        for i in range(len(self.item)):
            a.append([])
            for j in range(len(self.item)):
                if self.item[i][j] == True:
                    a[i].append(j)
        return a
                
    def adj_matrix_to_edge_list(self):
        e = []
        for i in range(len(self.item)):
            for j in range(len(self.item)):
                if self.item[i][j] == True:
                    e.append([i, j, 0])
        return e
        