# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 19:36:59 2021

@author: coderzparadise
"""
from Node import Node

class Trie(object):
    def __init__(self):
        self.root = Node()
        
    
    # overloading insert() and add() and append() function for easy-use
    def add(self, word):
        iter_node = self.root
        for c in word:
            if c not in iter_node.children:
                iter_node.children[c] = Node()
            iter_node = iter_node.children[c]
        iter_node.is_leaf = True
    
    # overloading insert() and add() and append() function for easy-use
    def insert(self, word):
        iter_node = self.root
        for c in word:
            if c not in iter_node.children:
                iter_node.children[c] = Node()
            iter_node = iter_node.children[c]
        iter_node.is_leaf = True
        
    # overloading insert() and add() and append() function for easy-use
    def append(self, word):
        iter_node = self.root
        for c in word:
            if c not in iter_node.children:
                iter_node.children[c] = Node()
            iter_node = iter_node.children[c]
        iter_node.is_leaf = True
    
    # Search for full word in Trie
    def search_word(self, word):
        iter_node = self.root
        for c in word:
            if c not in iter_node.children:
                return False
            iter_node = iter_node.children[c]
            
        if iter_node.is_leaf:
            return True
        return False
    
    # Search if prefix exists in Trie
    def is_prefix(self, word):
        iter_node = self.root
        for c in word:
            if c not in iter_node.children:
                return False
            iter_node = iter_node.children[c]
            
        return True
