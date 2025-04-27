# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 11:33:49 2021

@author: coderzparaise

Fastest time to implement code and explain Data Structure: Graph
    -11 minutes (each excluding dfs/bfs algo [extra 10 min each] )
"""

from AdjacencyList import AdjacencyList
from EdgeList import EdgeList
from AdjacencyMatrix import AdjacencyMatrix

if __name__ == "__main__":
    print('start program\n')
    
    n = ["Jack", "Dog", "Cat", "Bird", "Fish", "Lizzard"]
    
    ### Adjacency List
    print('\nAdj List')
    a = AdjacencyList(n)
    a.insert("Jack", "Cat")
    a.insert("Jack", "Dog")
    a.insert("Fish", "Dog")
    a.display()
    print( a.in_degree() )
    print('\n')
    e= a.adj_list_to_edge_list()
    print(e, '\n')
    
    am = a.adj_list_to_adj_matrix()
    print(am)
    
    ##########################
    
    
    ### Edge List
    print('\nEdge List')
    e = EdgeList(n)
    e.insert("Jack", "Fish")
    e.insert("Cat", "Dog")
    e.insert("Lizzard", "Bird")
    e.insert("Cat", "Fish")
    e.display()
    a = e.edge_list_to_adj_list()
    print(a, '\n')
    
    am = e.edge_list_to_adj_matrix()
    print(am)
    ##########################
    
    
    ### Adjacency Matrix
    print('\nAdj Matrix')
    am = AdjacencyMatrix(n)
    am.display()
    print()
    am.insert("Jack", "Fish")
    am.insert("Cat", "Dog")
    am.insert("Lizzard", "Bird")
    am.insert("Cat", "Fish")
    am.display()
    
    a = am.adj_matrix_to_adj_list()
    print(a)
    
    e = am.adj_matrix_to_edge_list()
    print(e)
    
    
