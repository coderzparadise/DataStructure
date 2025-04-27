# -*- coding: utf-8 -*-
"""
Created on Tue May 27 21:34:02 2021

@author: coderzparadise
"""

from Node import Node

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    # overloading insert() and add() function for easy-use
    def insert(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
            self.tail = self.head
        else:
            self.tail.next = Node(new_item)
            self.tail = self.tail.get_next()

    # overloading insert() and add() function for easy-use
    def add(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
            self.tail = self.head
        else:
            self.tail.next = Node(new_item)
            self.tail = self.tail.get_next()

    # overloading insert_after() and add_after() function for easy-use            
    def insert_after(self, new_item, key_item):
        if self == None or self.item == None:
            return
        
        iter_node = self.head
        while iter_node:
            if iter_node.get_item() == key_item:
                break
            iter_node = iter_node.get_item()
            
        if iter_node == None:
            return
        
        next_node = iter_node.get_next()
        insertee = Node(new_item, next_node)
        iter_node.next = insertee
        if next_node == None:
            self.tail = insertee   

    # overloading add_after() and insert_after() function for easy-use            
    def add_after(self, new_item, key_item):
        if self == None or self.item == None:
            return
        
        iter_node = self.head
        while iter_node:
            if iter_node.get_item() == key_item:
                break
            iter_node = iter_node.get_item()
            
        if iter_node == None:
            return
        
        next_node = iter_node.get_next()
        insertee = Node(new_item, next_node)
        iter_node.next = insertee
        if next_node == None:
            self.tail = insertee   
            
    # overloading insert_after() and add_after() function for easy-use   
    def insert_at_begin(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
            self.tail = self.head
        else:
            old_head = self.head
            insertee = Node(new_item, old_head)
            self.head = insertee

    # overloading add_after() and insert_after() function for easy-use   
    def add_at_begin(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
            self.tail = self.head
        else:
            old_head = self.head
            insertee = Node(new_item, old_head)
            self.head = insertee

    def reverse_list(self):
        if self == None or self.is_empty():
            return
        if self.head.get_next() == None:
            return
        
        prev = None
        curr_node = self.head
        soon_to_be_tail_node = curr_node # save our head, this will be our tail after reverse
        
        while curr_node != None:
            next_node = curr_node.get_next()
            curr_node.next = prev
            prev = curr_node
            curr_node = next_node
            
        #update head and tail
        self.head = prev
        self.tail = soon_to_be_tail_node
        

    def delete(self, key_item):
        if self == None or self.is_empty():
            return
        
        #check head node for key_item
        if self.head.get_item() == key_item:
            self.head = self.head.get_next()
            return
        
        iter_node = self.head
        while iter_node != None:
            if iter_node.get_item() == key_item:
                break
            prev = iter_node
            iter_node = iter_node.get_next()
        
        if iter_node == None:
            return
        
        prev.next = iter_node.get_next()
        if prev.get_next() == None:
            self.tail = prev    
            
        
    def remove_nth(self, n):
        slow = fast = self.head
        
        for i in range(n):
            fast = fast.get_next()
            # can also used: i != n-1
            if fast == None and i < n-1:
                return False
        
        if fast == None:
            self.head = self.head.get_next()
            return True
        
        while fast.get_next() != None:
            slow = slow.get_next()
            fast = fast.get_next()
        
        slow.next = slow.get_next().get_next()
        
        
    def remove_duplicates(self, key_item):
        if self == None or self.head == None:
            return
        prev = None
        iter_node = self.head
        while iter_node:
            if iter_node.get_item() == key_item:
                if prev == None:
                    self.head = self.head.get_next()
                    iter_node = iter_node.get_next()
                    
                else:
                    prev.next = iter_node.get_next()
                    if prev.next == None:
                        self.tail = prev
                        return
                    iter_node = prev.next
                    
            else:
                prev = iter_node
                iter_node = iter_node.get_next()
                
            
    def display(self):
        if self == None or self.head == None:
            return
        iter_node = self.head
        while iter_node != None:
            print(iter_node.get_item(), end = ' ')
            iter_node = iter_node.get_next()
        print()
        
        
    def is_empty(self):
        return self.head == None


    def get_list_length(self):
        if self.is_empty():
            return 0
        result = 0
        iter_node = self.head
        while iter_node != None:
            result += 1
            iter_node = iter_node.get_next()
        return result    
                
    
    def sort(self):
        self.head = self.merge_sort(self.head)
        
    def merge_sort(self, node):
        if node == None or node.get_next() == None:
            return node
        
        slow = node
        fast = slow
        while fast.next != None and fast.next.next != None:
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            
        after_mid = slow.next
        slow.next = None
        left = LinkedList.merge_sort(None, node)
        right = LinkedList.merge_sort(None, after_mid)
        return LinkedList.merge(None, left, right)
    
    def merge(self, left_head, right_head):
        if left_head == None:
            return right_head
        if right_head == None:
            return left_head
        result = None
        
        if left_head.get_item() < right_head.get_item():
            result = left_head
            result.next = LinkedList.merge(None, left_head.get_next(), right_head)
        else:
            result = right_head
            result.next = LinkedList.merge(None, left_head, right_head.get_next() )
        return result
                
    
    def get_intersect(self, list1, list2):
        len1 = len2 = 0
        p1 = list1.head
        p2 = list2.head
        while p1:
            len1+=1
            p1 = p1.get_next()
        
        while p2:
            len2 += 1
            p2 = p2.get_next()
        
        p1 = list1.head
        p2 = list2.head
        
        for i in range(abs(len1 - len2) ):
            if len1 > len2:
                p1 = p1.get_next()
            else:
                p2 = p2.get_next()
        
        #orginally I had (while p1 != p2) due to the fact of possible dup items as I wanted to compare address in memory rather than items
        while p1.get_item() != p2.get_item():
            p1 = p1.get_next()
            p2 = p2.get_next()
        
        return p1.get_item()
    

    def has_cycle(self):
        if self == None:
            return
        slow = fast = self.head
        
        while fast.get_next() != None and fast.get_next().get_next() != None:
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            if slow == fast:
                return True
        return False
    
    def begin_cycle(self):
        if self == None:
            return
        slow = fast = self.head
        
        while fast.get_next() != None and fast.get_next().get_next() != None:
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            if slow == fast:
                break
        if slow != fast:
            return
        slow = self.head
        while slow != fast:
            slow = slow.get_next()
            fast = fast.get_next()
        
        return slow.get_item()
    
    
    def odd_even_list(self):
        if self.head == None:
            return
        odd = self.head
        even = self.head.get_next()
        even_head = even
        
        while odd and even and odd.get_next() and even.get_next():
            odd.next = even.get_next()
            odd = odd.get_next()
            even.next = odd.get_next()
            even = even.get_next()
        
        odd.next = even_head
        
    
    def is_palindrome(self):
        if self.head.get_next() == None:
            return True
        
        fast = slow = self.head
        
        while fast != None and fast.get_next() != None:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow != None:
            next_node = slow.get_next()
            slow.next = prev
            prev = slow
            slow = next_node
        
        left = self.head
        right = prev
        
        while right:
            if left.get_item() != right.get_item():
                return False
            left = left.get_next()
            right = right.get_next()
        return True
    
    
    def rotate_list(self, k):
        if self.head == None or self.head.get_next() == None or k == 0:
            return
        
        iter_node = self.head
        list_len = 0
        
        while iter_node.get_next():
            list_len += 1
            iter_node = iter_node.get_next()
        list_len += 1
        
        rotate_num = k % list_len
        
        if rotate_num == 0:
            return
        
        iter_node.next = self.head
        iter_node = self.head
        
        i = 0
        while i < list_len - rotate_num - 1:
            i+=1
            iter_node = iter_node.get_next()
        
        next_node = iter_node.get_next()
        iter_node.next = None
        self.head = next_node
        self.tail = iter_node
            
    
    # ex.) 2 - 4 - 3  +  5 - 6 - 4  =  7 - 0 - 8
    #  342 + 465 = 807
    # Methods takes in two Lists and returns Nodes linked together (not a LinkedList)
    def add_two_nums(self, list1, list2):
        carry = 0
        place_holder = iter_node = Node(-1)
        list1 = list1.head
        list2 = list2.head
        
        while list1 or list2 or carry:
            v1 = v2 = 0
            if list1:
                v1 = list1.get_item()
                list1 = list1.get_next()
            if list2:
                v2 = list2.get_item()
                list2 = list2.get_next()
            
            insertee = v1+v2+carry
            iter_node.next = Node(insertee % 10)
            carry = insertee // 10
            iter_node = iter_node.next

        
        return place_holder.next
        
    
        