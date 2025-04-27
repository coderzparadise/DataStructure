# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 18:15:02 2021

@author: coderzparadise
"""

class Node(object):
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
    
    def get_item(self):
        return self.item
    
    def get_next(self):
        return self.next
    
    