# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 10:04:18 2021

@author: coderzparadise

Fastest time to implement code and explain Data Structure: LinkedList
    -140 minutes
"""

class Node(object):
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
    
    def get_item(self):
        return self.item
    
    def get_next(self):
        return self.next
    

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head == None
    
    def display(self):
        if self.is_empty():
            return
        
        iter_node = self.head
        while iter_node:
            print(iter_node.get_item(), end = ' ')
            iter_node = iter_node.get_next()
        print()
    
    def insert(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
            self.tail = self.head
        else:
            self.tail.next = Node(new_item)
            self.tail = self.tail.get_next()
    
    def insert_at_begin(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
            self.tail = self.head
        else:
            old_head = self.head
            insertee = Node(new_item)
            insertee.next = old_head
            self.head = insertee
            
    def insert_after(self, new_item, key_item):
        if self.is_empty():
            return
        
        iter_node = self.head
        while iter_node != None:
            if iter_node.get_item() == key_item:
                break
            iter_node = iter_node.get_next()
        
        if iter_node == None:
            return
        
        
        insertee = Node(new_item)
        next_node = iter_node.get_next()
        
        iter_node.next = insertee
        
        if next_node == None:
            self.tail = insertee
            return
        
        insertee.next = next_node
        
    
    def reverse(self):
        if self.is_empty() or self.head.get_next() == None:
            return
        
        prev = None
        iter_node = self.head
        old_head = iter_node
        
        while iter_node:
            next_node = iter_node.get_next()
            iter_node.next = prev
            prev = iter_node
            iter_node = next_node
        
        self.tail = old_head
        self.head = prev
    
    # PRACTICE
    def delete(self, key_item):
        if self.is_empty():
            return
        
        if self.head.get_item() == key_item:
            self.head = self.head.get_next()
            return
        
        iter_node = self.head
        prev = None
        
        while iter_node:
            if iter_node.get_item() == key_item:
                break
            prev = iter_node
            iter_node = iter_node.get_next()
            
        if iter_node == None:
            return
        
        next_node = iter_node.get_next()
        if next_node == None:
            prev.next = None
            self.tail = prev
            return
        prev.next = next_node
        
    # PRACTICE!
    def remove_nth(self, n):
        if self.is_empty() or n <= 0:
            return
        
        slow = fast = self.head
        
        for i in range(n):
            fast = fast.get_next()
            if fast == None:
                if i == n-1:
                    self.head = self.head.get_next()
                    return
                return
        
        while fast.get_next():
            slow = slow.get_next()
            fast = fast.get_next()
        
        next_node = slow.get_next().get_next()
        if next_node == None:
            slow.next = None
            self.tail = slow
            return
        slow.next = next_node
        
                
    # PRACTICE !
    def remove_duplicates(self, key_item):
        if self.is_empty():
            return
        prev = None
        iter_node = self.head
  
        while iter_node:
            if iter_node.get_item() == key_item:
                if prev == None:
                    iter_node = iter_node.get_next()
                    self.head = self.head.get_next()
                else:
                    prev.next = iter_node.get_next()
                    if prev.next == None:
                        self.tail = prev
                        return
                    iter_node = prev.next
            else:
                prev = iter_node
                iter_node = iter_node.get_next()
        
        
    
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
            result.next = self.merge(left.get_next(), right)
        else:
            result = right
            result.next = self.merge(left, right.get_next() )
        
        return result
            
    
    def get_intersect(self, list1, list2):
        p1 = list1.head
        p2 = list2.head
        
        len1 = len2 = 0
        
        while p1:
            p1 = p1.get_next()
            len1 += 1
            
        while p2:
            p2 = p2.get_next()
            len2 += 1
        
        p1 = list1.head
        p2 = list2.head
        
        for i in range( abs(len1 - len2) ):
            if len1 < len2:
                p2 = p2.get_next()
            else:
                p1 = p1.get_next()
        
        while p1.get_item() != p2.get_item():
            p1 = p1.get_next()
            p2 = p2.get_next()
            if p1 == None or p2 == None:
                return 
        
        return p1.get_item()
        
    def has_cycle(self):
        if self.is_empty() or self.head.get_next():
            return False
        slow = fast = self.head
        while fast.get_next() and fast.get_next().get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            if slow == fast:
                return True
        return False
    
    # PRACTICE!
    def begin_of_cycle(self):
        if self.is_empty() or self.head.get_next() == None:
            return False
        slow = fast = self.head
        while fast.get_next() and fast.get_next().get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            if slow == fast:
                break
        
        if slow == fast:
            slow = self.head
            while fast != slow:
                fast = fast.get_next()
                slow = slow.get_next()
                
            return slow.get_item()
        
        
    def odd_even_list(self):
        if self.is_empty():
            return
        
        odd = self.head
        even = odd.next
        even_head = even
        
        while odd and even and odd.get_next() and even.get_next():
            odd.next = even.get_next()
            odd = odd.get_next()
            even.next = odd.get_next()
            even = even.get_next()
        
        odd.next = even_head
        
        
    
    def is_palidrome(self):
        if self.is_empty() or self.head.get_next() == None:
            return True
        
        slow = fast = self.head
        while fast and fast.get_next():
            fast = fast.get_next().get_next()
            slow = slow.get_next()
        
        prev = None
        while slow:
            next_node = slow.get_next()
            slow.next = prev
            prev = slow
            slow = next_node
        
        start = self.head
        while prev:
            if start.get_item() != prev.get_item():
                return False
            start = start.get_next()
            prev = prev.next
        
        return True
    
    
    def rotate_list(self, k):
        if self.is_empty() or self.head.get_next() == None or k == 0:
            return
        list_len = 0
        iter_node = self.head
        while iter_node.get_next():
            iter_node = iter_node.get_next()
            list_len+=1
        list_len +=1
        
        if k % list_len == 0:
            return
        
        k = k% list_len
        
        iter_node.next = self.head
        iter_node = self.head
        
        for i in range( list_len - 1 - k):
            iter_node = iter_node.get_next()
        
        next_node = iter_node.get_next()
        iter_node.next = None
        self.tail = iter_node
        self.head = next_node
        
    
    def add_two_nums(self, list1, list2):
        carry = 0
        list1 = list1.head
        list2 = list2.head
        
        iter_node = start = Node(-1)
        
        while list1 or list2 or carry:
            v3 = 0
            
            if list1:
                v3 += list1.get_item()
                list1 = list1.get_next()
                
            if list2:
                v3 += list2.get_item()
                list2 = list2.get_next()
            
            v3 += carry
            iter_node.next = Node(v3%10)
            carry = v3 // 10
            iter_node = iter_node.get_next()
            
        return start.get_next()
    

        
        
        
                
                
    
    
    
if __name__ == "__main__":
    print('start\n')
    ll = LinkedList()
    ll.insert(30)
    ll.insert(45)
    ll.insert(8)
    ll.insert(3)
    ll.insert(37)
    ll.insert(99)
    ll.display()
    # ll.insert_at_begin(5)
    ll.insert(75)
    ll.insert(90)
    ll.display()
    # ll.insert_after(25, 19)
    # ll.display()
    # ll.reverse()
    # ll.display()
    # ll.insert(11)
    # ll.display()
    # ll.delete(33)
    # ll.insert(32)
    # ll.display()
    # ll.remove_nth(5)
    # ll.display()
    # ll.remove_duplicates(32)
    # ll.display()
    # ll.insert(77)
    # ll.display()
    
    # # ll.sort()
    # # ll.display()
    print( ll.is_palidrome() )
    ll.display()
    ll.rotate_list(2)
    ll.display()
    ll.insert(44)
    ll.display()
    ll.sort()
    ll.display()
    
    