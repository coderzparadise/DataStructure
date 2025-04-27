# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 15:37:17 2021

@author: coderzparadise

Fastest time to implement code and explain Data Structure: LinkedList
    -80 minutes
"""

class Node(object):
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
    
    def get_next(self):
        return self.next
    
    def get_item(self):
        return self.item
    

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def is_empty(self):
        return self.head == None
    
    def insert(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
            self.tail = self.head
        else:
            self.tail.next = Node(new_item)
            self.tail = self.tail.get_next()
    
    
    
    def sum_list(self, list1, list2):
        carry = 0
        list1 = list1.head
        list2 = list2.head
        
        holder = Node(-1)
        temp = holder
        
        while list1 or list2 or carry:
            v3 = 0
            
            if list1:
                v3 += list1.get_item()
                list1 = list1.get_next()
            
            if list2:
                v3 += list2.get_item()
                list2 = list2.get_next()
                
            v3 = v3 + carry
            temp.next = Node(v3%10)
            temp = temp.get_next()
            carry = v3 // 10
        
        return holder.get_next()
    
    
    def rotate_list(self, k):
        if self.is_empty() or k == 0:
            return
        
        list_len = 0
        iter_node = self.head
        
        while iter_node.get_next():
            list_len += 1
            iter_node = iter_node.get_next()
        list_len += 1
        
        if k % list_len == 0:
            return
        
        k = k % list_len
        
        iter_node.next = self.head
        iter_node = self.head
        for i in range(list_len - 1 - k):
            iter_node = iter_node.get_next()
            
        next_node = iter_node.get_next()
        self.head = next_node
        self.tail = iter_node
        iter_node.next = None
        
        
    def is_palindrone(self):
        if self.head == None or self.head.next == None:
            return True
        
        slow = fast = self.head
        
        while fast and fast.get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            
        prev = None
        while slow:
            next_node = slow.get_next()
            slow.next = prev
            prev = slow
            slow = next_node
        
        slow = self.head
        
        while prev:
            if slow.get_item() != prev.get_item():
                return False
            slow = slow.get_next()
            prev = prev.get_next()
        
        return True
    
    
    def even_odd_list(self):
        if self.is_empty() or self.head.get_next() == None:
            return
        
        odd = self.head
        even = self.head.get_next()
        even_head = even
        
        while even and odd and even.get_next() and odd.get_next():
            odd.next = even.get_next()
            odd = odd.get_next()
            even.next = odd.get_next()
            even = even.get_next()
        
        odd.next = even_head
        
    
    def start_of_cycle(self):
        if self.is_empty() or self.head.get_next() == None:
            return
        
        slow = fast = self.head
        
        while fast.get_next() and fast.get_next().get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            if slow == fast:
                break
            
        if fast.get_next() == None or fast.get_next().get_next() == None:
            return 
        
        slow = self.head
        
        while slow != fast:
            slow = slow.get_next()
            fast = fast.get_next()
        
        return slow.get_item()
        
    
    def get_intersect(self, list1, list2):
        list1 = list1.head
        list2 = list2.head
        
        len1 = len2 = 0
        
        while list1:
            len1 += 1
            list1 = list1.get_next()
        
        while list2:
            len2 += 1
            list2 = list2.get_next()
        
        list1 = list1.head
        list2 = list2.head
        
        for i in range(abs(len1 - len2) ):
            if len1 > len2:
                list1 = list1.get_next()
            else:
                list2 = list2.get_next()
        
        while list1.get_item() != list2.get_item():
            list1 = list1.get_next()
            list2 = list2.get_next()
            if list1 == None or list2 == None:
                return None
        
        return list1.get_item()
    
    
    def remove_elements(self, target):
        if self.is_empty():
            return
        
        prev = None
        iter_node = self.head
        
        while iter_node:
            if iter_node.get_item() == target:
                if prev == None:
                    self.head = self.head.get_next()
                    iter_node = iter_node.get_next()
                else:
                    next_node = iter_node.get_next()
                    prev.next = next_node
                    if next_node == None:
                        self.tail = prev
                    iter_node = next_node
            else:
                prev = iter_node
                iter_node = iter_node.get_next()
                
                
    
    def remove_nth(self, n):
        if self.is_empty():
            return
        
        slow = fast = self.head
        
        for i in range(n):
            fast = fast.get_next()
            if fast == None and i < n-1:
                return None
        
        if fast == None:
            self.head = self.head.get_next()
            return
        
        while fast.get_next():
            slow = slow.get_next()
            fast = fast.get_next()
        
        next_node = slow.get_next().get_next()
        if next_node == None:
            self.tail = slow
        slow.next = next_node
        
        
    def reverse(self):
        if self.is_empty() or self.head.get_next() == None:
            return
        
        iter_node = old_head = self.head
        prev = None
        
        while iter_node:
            next_node = iter_node.get_next()
            iter_node.next = prev
            prev = iter_node
            iter_node = next_node
            
        self.tail = old_head
        self.head = prev
        
        
    def delete(self, key):
        if self.is_empty():
            return
        
        if self.head.get_item() == key:
            self.head = self.head.get_next()
            return
        
        iter_node = self.head
        prev = None
        
        while iter_node:
            if iter_node.get_item() == key:
                break
            prev = iter_node
            iter_node = iter_node.get_next()
            
        if iter_node == None:
            return
        
        
        prev.next = iter_node.get_next()
        if prev.next == None:
            self.tail = prev
            
    def insert_after(self, new_item, key):
        if self.is_empty():
            return
        
        iter_node = self.head
        
        while iter_node:
            if iter_node.get_item() == key:
                break
            iter_node = iter_node.get_next()
        
        if iter_node == None:
            return
        
        next_node = iter_node.get_next()
        insertee = Node(new_item, next_node)
        iter_node.next = insertee
        if next_node == None:
            self.tail = insertee
    
    
    def sort(self):
        self.head = self.merge_sort(self.head)
        
    def merge_sort(self, node):
        if node == None or node.get_next() == None:
            return node
        
        slow = fast = node
        while fast.get_next() and fast.get_next().get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            
        after_mid = slow.get_next()
        slow.next = None
        
        left = self.merge_sort(node)
        right = self.merge_sort(after_mid)
        
        return self.merge(left, right)
    
    def merge(self, left, right):
        if left == None:
            return right
        
        if right == None:
            return left
        
        result = None
        
        if left.get_item() < right.get_item():
            result = left
            result.next = self.merge(left.get_next(), right )
        else:
            result = right
            result.next = self.merge(left, right.get_next() )
            
        return result
        

def merge_sort2(node):
    if node == None or node.get_next() == None:
        return node
    
    slow = fast = node
    while fast.get_next() and fast.get_next().get_next():
        slow = slow.get_next()
        fast = fast.get_next().get_next()
        
    after_mid = slow.get_next()
    slow.next = None
    
    left = merge_sort2(node)
    right = merge_sort2(after_mid)
    
    return merge2(left, right)

def merge2(left, right):
    holder = temp = Node(-1)
    
    while left and right:
        if left.get_item() < right.get_item():
            temp.next = left
            left = left.get_next()
        else:
            temp.next = right
            right = right.get_next()
        
    
    while left:
        temp.next = Node(left.get_item() )
        temp = temp.get_next()
        left = left.get_next()
    
    while right:
        temp.next = Node(right.get_item() )
        temp = temp.get_next()
        right = right.get_next()
        
    return holder.get_next()
        
        
        
        
        
        
        
        
        
        
        
            
            
        
            
            
        
        