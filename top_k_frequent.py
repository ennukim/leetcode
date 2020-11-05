#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 23:46:36 2020

@author: sallykim
"""

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    d = dict()
    lst = []
    ans = []
    for elem in nums:
        if elem in d:
            d[elem] += 1
        else:
            d[elem] = 1
    
    
    for value in d.values():
        lst.append(value)
        
    for i in range(k):
        print(max(lst))
        ans.append(max(lst))
        lst.pop(lst.index(max(lst)))
        
    return ans

from collections import Counter  
import heapq

def topKFrequent2(nums, k):
    if len(nums) == k:
        return nums
    c = Counter(nums) # O(n)
    
    return heapq.nlargest(k, c.keys(), key=c.get)

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent2(nums, k))
