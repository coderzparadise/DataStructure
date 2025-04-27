# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 22:27:56 2021

@author: coderzparadise

Fastest time to complete and explain: 19 minutes

"""
class Node(object):
    def __init__(self, item = None):
        self.children = {}
        self.is_leaf = False

class Trie(object):
    def __init__(self):
        
        self.root = Node()
    
    def insert(self, word):
        iter_node = self.root
        for c in word:
            if c not in iter_node.children:
                iter_node.children[c] = Node()
            iter_node = iter_node.children[c]
        iter_node.is_leaf = True
    
    def search(self, word):
        iter_node = self.root
        for c in word:
            if c not in iter_node.children:
                return False
            iter_node = iter_node.children[c]
        if iter_node.is_leaf == True:
            return True
        return False
    

if __name__ == "__main__":
    print('start program\n')
    t = Trie()
    t.insert('soccer')
    t.insert('socks')
    print(t.search('soccer') )
            
            