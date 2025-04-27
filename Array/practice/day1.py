# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 21:34:25 2021

@author: coderzparadise

Fastest time to complete and explain: 12 minutes
"""

def merge_sort(nums):
    if not nums or len(nums) <= 1:
        return
    
    mid = len(nums) // 2
    
    left = nums[:mid]
    right = nums[mid:]
    
    merge_sort(left)
    merge_sort(right)
    
    lp = rp = ip = 0
    
    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            nums[ip] = left[lp]
            lp += 1
        else:
            nums[ip] = right[rp]
            rp += 1
        ip += 1
        
    while lp < len(nums):
        nums[ip] = left[lp]
        lp += 1
        ip += 1
    
    while rp < len(nums):
        nums[ip] = right[rp]
        rp += 1
        ip += 1
    

if __name__ == "__main__":
    print('start\n')
    
    q1 = [40,23,7,90,50,10,21,8]
    print(q1)
    merge_sort(q1)
    # print(q1)
    
