# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 12:46:49 2021

@author: coderzparadise

Fastest time to implement code and explain Data Structure: Graph
    -34 minutes
"""

class Adj_list(object):
    
    def __init__(self, nodes):
        self.item = []
        for i in range(len(nodes) ):
            self.item.append([] )
        
    def insert(self, index1, index2):
        self.item[index1].append(index2)
    
    def display(self):
        print(self.item)
    
    def in_degree(self):
        res = [0] * len(self.item)
        
        for i in range(len(self.item) ):
            for j in range(len(self.item[i]) ):
                res[ self.item[i][j] ] += 1
        return res
    
    def bfs(self, src):
        queue = []
        visited = []
        res = []
        visited.append(src)
        queue.append(src)
        
        while queue:
            cur = queue.pop(0)
            res.append(cur)
            
            for i in self.item[cur]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)
                    prev[i] = cur
                    
    def topological(self):
        res = []
        queue = []
        indegree = self.in_degree()
        
        for i in range(len(indegree) ):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            cur = queue.pop(0)
            res.append(cur)
            
            for i in range(len(self.item[cur]) ):
                indegree[self.item[cur][i] ] -= 1
                if indegree[self.item[cur][i]] == 0:
                    queue.append(self.item[cur][i] )
                    
        if len(self.item) == len(res):
            return res
        return []
    
    
class Edge_list(object):
    def __init__(self):
        self.item = []
    
    def insert(self, index1, index2):
        self.item.append( [index1, index2, 0])
    
    def display(self):
        print(self.item)
        
    def kruskal(self):
        res = []
        self.item = sorted(self.item, key = lambda x:x[2] )
        d = DSF(len(self.item) )
        
        for e in self.item:
            if not d.check_same_set(e[0], e[1] ):
                d.union(e[0], e[1] )
                res.append( e )
        return res
            
        
        
        
        
    