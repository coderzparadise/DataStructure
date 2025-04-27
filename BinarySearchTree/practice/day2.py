# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 12:10:19 2021

@author: coderzparadise

Fastest time to complete and explain: 55 minutes
"""

class BST(object):
    def __init__(self, item = None):
        self.item = item
        self.left = None
        self.right = None
    
    def display(self, space):
        if self == None:
            return
        BST.display(self.right, space + '   ')
        print(space , self.item)
        BST.display(self.left, space+ '   ')
    
    def insert(self, new_item):
        if self.item == None:
            self.item = new_item
        else:
            if self.item > new_item:
                if self.left == None:
                    self.left = BST(new_item)
                else:
                    BST.insert(self.left, new_item)
            else:
                if self.right == None:
                    self.right = BST(new_item)
                else:
                    BST.insert(self.right, new_item)
                    
    def sum_nodes(self):
        if self == None or self.item == None:
            return
        return self.item + BST.sum_nodes(self.left) + BST.sum_nodes(self.right)
    
    def num_nodes(self):
        if self == None or self.item == None:
            return
        return 1 + BST.num_nodes(self.left) + BST.num_nodes(self.right)
    
    def sum_at_depth(self, depth):
        if self == None or self.item == None:
            return 0
        if depth == 0:
            return self.item
        return BST.sum_at_depth(self.left, depth - 1) + BST.sum_at_depth(self.right, depth - 1)
    
    def smallest(self):
        if self == None or self.item == None:
            return
        if self.left != None:
            return BST.smallest(self.left)
        else:
            return self.item
    
    def largest(self):
        if self == None or self.item == None:
            return
        if self.right != None:
            BST.largest(self.right)
        else:
            return self.item
    
    def print_at_depth(self, depth):
        if self == None or self.item == None:
            return
        if depth == 0:
            print( self.item )
        
        BST.print_at_depth(self.left, depth - 1)
        BST.print_at_depth(self.right, depth - 1)
    
    
    def height(self):
        if self == None or self.item == None:
            return 0
        
        left = BST.height(self.left)
        right = BST.height(self.right)
        
        if self.left == None and self.right == None:
            return max(left, right)
        
        if left > right:
            return left + 1
        return right + 1
    
    
    def depth_of_item(self, key):
        if self == None or self.item == None:
            return -1
        
        if self.item == key:
            return 0
        
        elif self.item < key:
            d = BST.depth_of_item(self.right)
        else:
            d = BST.depth_of_item(self.left)
        
        if d < 0:
            return -1
        return d + 1
    
    
    def build_BST(self, my_list):
        if len(my_list) == 0:
            return
        
        mid = len(my_list) // 2
        self = BST(my_list[mid] )
        self.left = BST.build_BST(my_list[:mid])
        self.right = BST.build_BST(my_list[mid+1:])
        
        return self
    
    
    def lowest_common(self, integer1, integer2):
        if self == None:
            return
        
        if self.item < min(integer1, integer2):
            return BST.lowest_common(self.right, integer1, integer2)
        
        elif self.item > max(integer1, integer2):
            return BST.lowest_common(self.left, integer1, integer2)
        
        return self.item
        
    
    def kth_num(self, k):
        stack = []
        stack.append(self)
        
        while stack or self:
            while self:
                stack.append(self)
                self = self.left
            self = stack.pop()
            
            k -= 1
            if k == 0:
                return self.item
        
            self = self.right
    
    def preorder_iter(self):
        stack = []
        stack.append(self)
        visited = []
        while stack:
            curr = stack.pop()
            if curr:
                if curr in visited:
                    result.append(curr.item)
                else:
                    visited.append(curr)
                    stack.append(curr.right)
                    stack.append(curr.left)
                    stack.append(curr)
        return result
    
    def inorder_iter(self):
        stack = []
        stack.append(self)
        result = []
        visited = []
        
        while stack:
            curr = stack.pop()
            if curr:
                if curr not in visited:
                    visited.append(curr)
                    stack.append(curr.right)
                    stack.append(curr)
                    stack.append(curr.left)
                else:
                    result.append(curr.item)
        return result
    
    
    def right_side(self):
        result = []
        queue = []
        queue.append(self)
        while queue:
            r_len = len(queue)
            right_side = None
            
            for i in range(r_len):
                node = queue.pop(0)
                if node:
                    right_side = node
                    queue.append(node.left)
                    queue.append(node.right)
            if right_side:
                result.append(right_side.item)
        
        return result
                
            
    



if __name__ == "__main__":
    print('start\n')
    b = BST()
    b.insert(7)
    b.insert(39)
    b.insert(25)
    b.insert(2)
    b.insert(4)
    b.insert(53)
    b.insert(1)
    b.insert(59)
    b.display('')