# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 12:13:44 2021
@author: coderzparadise
"""

class BST(object):
    def __init__(self, new_item = None):
        self.item = new_item
        self.left = None
        self.right = None
        
    def get_item(self):
        return self.item

    # overloading insert() and add() function for easy-use
    def insert(self, new_item):
        if self.item == None:
            self.item = new_item
        else:
            if new_item < self.item:
                if self.left == None:
                    self.left = BST(new_item)
                else:
                    BST.insert(self.left, new_item)
            else:
                if self.right == None:
                    self.right = BST(new_item)
                else:
                    BST.insert(self.right, new_item)

    # overloading add() and insert() function for easy-use
    def add(self, new_item):
        if self.item == None:
            self.item = new_item
        else:
            if new_item < self.item:
                if self.left == None:
                    self.left = BST(new_item)
                else:
                    BST.insert(self.left, new_item)
            else:
                if self.right == None:
                    self.right = BST(new_item)
                else:
                    BST.insert(self.right, new_item)
        
    def display(self, space):
        if self == None or self.item == None:
            return
        BST.display(self.right, space + '   ')
        print(space, self.get_item() )
        BST.display(self.left, space + '   ')
        
    def sum_at_depth(self, depth):
        if self == None:
            return 0
        if depth == 0:
            return self.get_item()
        return BST.sum_at_depth(self.left, depth-1) + BST.sum_at_depth(self.right, depth-1)
    
    def find_depth_of_item(self, key_item):
        if self == None or self.item == None:
            return -1
        if self.get_item() == key_item:
            return 0
        if key_item < self.get_item():
            d =  BST.find_depth_of_item(self.left, key_item)
        else:
            d = BST.find_depth_of_item(self.right, key_item) 
        
        if d < 0:
            return -1
        else:
            return d+1    
    
    def smallest(self):
        if self == None or self.item == None:
            return
        if self.left == None:
            return self.get_item()
        return BST.smallest(self.left)
    
    def largest(self):
        if self == None or self.item == None:
            return
        if self.right == None:
            return self.get_item()
        return BST.largest(self.right)
    
    def find(self, key_item):
        if self == None or self.get_item() == None:
            return False
        if self.get_item() == key_item:
            return True
        if key_item < self.get_item():
            return BST.find(self.left, key_item)
        return BST.find(self.right, key_item)
    
    def print_at_depth(self, depth):
        if self == None or self.item == None:
            return
        elif depth == 0:
            print(self.get_item(), end = ' ' )
        BST.print_at_depth(self.left, depth-1)
        BST.print_at_depth(self.right, depth-1)   
        
    def sum_of_nodes(self):
        if self == None or self.get_item() == None:
            return 0
        return self.get_item() + BST.sum_of_nodes(self.left) + BST.sum_of_nodes(self.right)
    
    def num_of_nodes(self):
        if self == None or self.get_item() == None:
            return 0
        return 1 + BST.num_of_nodes(self.left) + BST.num_of_nodes(self.right)
    
    def extract_to_list(self, result):
        if self == None:
            return
        BST.extract_to_list(self.left, result)
        result.append(self.get_item() )
        BST.extract_to_list(self.right, result)
        
        
    ### PRACTICE!! ###
    def build_BST(self, list_of_item):
        if list_of_item == None or len(list_of_item) == 0:
            return
        mid_index = len(list_of_item) // 2
        self = BST(list_of_item[mid_index] )
        
        self.left = BST.build_BST(self.left, list_of_item[:mid_index])
        self.right = BST.build_BST(self.right, list_of_item[mid_index+1:])
        
        # These 2 lines work as well
        # self.left = self.build_BST(my_list[:mid] )
        # self.right = self.build_BST(my_list[mid+1:] )
        return self        
    
    ### PRACTICE!! ###
    def height(self):
        if self == None or self.get_item() == None:
            return 0
        
        left_sub_tree_height = BST.height(self.left)
        right_sub_tree_height = BST.height(self.right)
        
        if self.left == None and self.right == None:
            return max(left_sub_tree_height, right_sub_tree_height)
        
        if left_sub_tree_height > right_sub_tree_height:
            return left_sub_tree_height + 1
        return right_sub_tree_height + 1
    
    
    def preorder_iter(self):
        stack = []
        visited = []
        preorder = []
        stack.append(self)
        while stack:
            curr = stack.pop()
            if curr:
                if curr in visited:
                    preorder.append(curr.item)
                else:
                    stack.append(curr.right)
                    stack.append(curr.left)
                    stack.append(curr)
                    visited.append(curr)
        return preorder
    
    def inorder_iter(self):
        stack = []
        visited = []
        inorder = []
        stack.append(self)
        while stack:
            curr = stack.pop()
            if curr:
                if curr in visited:
                    inorder.append(curr.item)
                else:
                    stack.append(curr.right)
                    stack.append(curr)
                    stack.append(curr.left)
                    visited.append(curr)
        return inorder
    
    def postorder_iter(self):
        stack = []
        visited = []
        post = []
        stack.append(self)
        while stack:
            curr = stack.pop()
            if curr:
                if curr in visited:
                    post.append(curr.item)
                else:
                    stack.append(curr)
                    stack.append(curr.right)
                    stack.append(curr.left)
                    visited.append(curr)
        return post
    
    def lowest_common_ancestor(self, integer1, integer2):
        if self == None or self.item == None:
            return
        elif self.item > max(integer1, integer2):
            return BST.lowest_common_ancestor(self.left, integer1, integer2)
        elif self.item < min(integer1, integer2):
            return BST.lowest_common_ancestor(self.right, integer1, integer2)
        return self.item
    
    
    def kth_num(self, k):
        stack = []
        
        while stack or self.item:
            
            #if you go off the deep end, self will not have a 'self.item' so use 'self'
            while self:
                stack.append(self)
                self = self.left
            
            #get node
            self = stack.pop()
            k -=1
            if k == 0:
                return self.item
            
            #go right
            self = self.right
        
        