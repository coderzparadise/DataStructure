# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 11:35:35 2021

@author: coderzparadie
"""
import numpy as np


class DisjointForrestSet(object):
    def __init__(self, size):
        self.item = np.zeros(size, dtype=int)-1
    
    def display(self):
        print(self.item)
        
     #Find with path
    def find_root(self, index):
        if self.item[index] < 0:
            return index
        return self.find_root( self.item[index] )

    #Union by Size
    def union(self, i, j):
        ri = self.find_root(i)
        rj = self.find_root(j)
        #checks if in same subset
        if ri != rj:
            #Checks which dsf is smalller
            
            if self.item[ri] > self.item[rj]:
                self.item[rj] += self.item[ri]  #sum up both and store in least [rj]
                self.item[ri] = rj #tell the greater one [ri] where the least  [ri] one is
            else:
                self.item[ri] += self.item[rj]
                self.item[rj] = ri            
                
    def check_same_set(self, i, j):
        root1 = self.find_root(i)
        root2 = self.find_root(j)
        if root1 != root2:
            return False
        return True

                    
##################################
##################################
class EdgeList(object):
    def __init__(self, nodes):
        self.node = nodes
        self.item = []
        self.num_of_nodes = len(self.node)
        
    def insert(self, item1, item2):
        if item1 in self.node and item2 in self.node:
            index1 = self.node.index(item1)
            index2 = self.node.index(item2)
            self.item.append([index1,index2])
        else:
            index1 = item1
            index2 = item2
            self.item.append([index1,index2])
            
    def insert_list(self, new_list):
        for i in new_list:
            self.item.append([i[0], i[1], i[2]])
        
    def display(self):
        print(self.item)
        
    def edge_list_to_adj_matrix(self):
        m = np.zeros((self.num_of_nodes, self.num_of_nodes), dtype=bool)
        for i in range(len(self.item) ):
            m[self.item[i][0]][self.item[i][1]] = True
            # m[self.item[i][1]][self.item[i][0]] = True  # For undirected graph
        return m
    
    
    # edge_list = self.item[edge1,edge1,weight]
    def kruskal(self):
        self.item = sorted(self.item, key=lambda a: a[2]) # practice "key"=lambda
        ds = DisjointForrestSet(len(self.item))
        min_span_tree = []
        for edge in self.item:
            if ds.check_same_set(edge[0], edge[1]) == False:
                min_span_tree.append(edge)
                ds.union(edge[0], edge[1])
        return min_span_tree        
    
        
    

if __name__ == "__main__":
    print('start program\n')

    #Kruskal Function
    
    n = [1, 2, 3, 4, 5, 6, 7]
    e_list = [ [1,2,28], [2,3,16], [3,4,12], [4,5,22], [5,6,25], [6,1,10], [2,7,14], [7,5,24], [7,4,18] ]
    e = EdgeList(n)
    
    e.insert_list(e_list)
    
    print( e.kruskal() )
    
    
    