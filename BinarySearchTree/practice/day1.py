# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 10:12:55 2021

@author: coderzparadise

Fastest time to complete and explain: 58 minutes
"""

class BST(object):
    def __init__(self, item = None):
        self.item = item
        self.left = None
        self.right = None
        
    def get_item(self):
        return self.item
    
    def is_empty(self):
        return self.item == None
    
    def insert(self, new_item):
        if self.is_empty():
            self.item = new_item
        else:
            if self.get_item() < new_item:
                if self.right == None:
                    self.right = BST(new_item)
                else:
                    BST.insert(self.right, new_item)
            else:
                if self.left == None:
                    self.left = BST(new_item)
                else:
                    BST.insert(self.left, new_item)
    #PRACTICE           
    def display(self, space):
        if self == None or self.get_item() == None:
            return
        BST.display(self.right, space+'   ')
        print(space, self.get_item() )
        BST.display(self.left, space+'   ')
    
    def depth_of_item(self, key_item):
        if self == None or self.is_empty():
            return -1
        
        if self.get_item() == key_item:
            return 0
        
        if self.get_item() < key_item:
            d = BST.depth_of_item(self.right, key_item)
        else:
            d = BST.depth_of_item(self.left, key_item)
        
        if d < 0:
            return -1
        return d + 1
    
    #PRACTICE
    def build_BST(self, my_list):
        if len(my_list) == 0:
            return 
        
        mid = len(my_list) // 2
        self = BST( my_list[mid])
        self.left = self.build_BST(my_list[:mid] )
        self.right = self.build_BST(my_list[mid+1:] )
        return self
                
    
    def height(self):
        if self == None or self.get_item() == None:
            return 0
        left = BST.height(self.left)
        right = BST.height(self.right)
        
        if self.left == None and self.right == None:
            return max(left, right)
        
        if left > right:
            return left + 1
        return right + 1
    
    def lowest_common(self, integer1, integer2):
        if self == None or self.get_item() == None:
            return
        
        if self.get_item() < min(integer1, integer2):
            return BST.lowest_common(self.right, integer1, integer2)
        elif self.get_item() > max(integer1, integer2):
            return BST.lowest_common(self.left, integer1, integer2)
        return self.get_item()
    
    #Practice!
    def kth_num(self, k):
        stack = []
        stack.append(self)
        while stack or self.get_item():
            while self:
                stack.append(self)
                self = self.left
                
            self = stack.pop()
            k -= 1
            if k == 0:
                return self.get_item()
            
            self = self.right
        return
    
    # PRACTICE
    def inorder_iter(self):
        if self == None or self.get_item() == None:
            return
        stack = []
        result = []
        visited  = []
        stack.append(self)
        
        while stack:
            curr = stack.pop()
            if curr:
                if curr in visited:
                    result.append(curr.get_item() )
                else:
                    visited.append(curr)
                    stack.append(curr.right)
                    stack.append(curr)
                    stack.append(curr.left)
                
        return result
        


if __name__ == "__main__":
    print('start\n')
    b = BST()
    b.insert(5)
    b.insert(9)
    b.insert(8)
    b.insert(14)
    b.insert(1)
    b.insert(2)
    print('b')
    b.display('')
    print('\n')
    # print(b.depth_of_item(1) )
    
    money = [2, 4, 15, 18, 37, 44, 202, 247, 415]
    t = BST.build_BST(None, money)
    print('t')
    t.display('')
    print()
    print( 'b height: ', b.height() )
    print('t height: ', t.height() )
    print('lowest common: ', b.lowest_common(8,10))
    print( 'b kthn num: ', b.kth_num(3) )
    
    l2 = b.inorder_iter()
    print(l2)
            