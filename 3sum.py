"""
Created on Mon Jun 15 01:07:41 2020
Tried again on Tue Oct 20, 2020
@author: sallykim
"""

#   My initial try
#   Time complexity - O(nlogn + n^2)
#       sort() - O(nlogn)
#       pointer function - O(n)
#       for loop - n times 

def threeSum(nums):
    res = []
    nums.sort()
    length = len(nums)
    for i in range(length-2):
        if nums[i] > 0: break
        #   the second comparison condition avoids 
        #   an unnecessary run that has been done previously
        if i > 0 and nums[i]==nums[i-1]: continue
    
        left, right = i+1, length-1
        while left < right:
            total = nums[i]+nums[left]+nums[right]
            if total < 0:
                left += 1 
            elif total > 0:
                right -= 1
            else:
                res.append([nums[i],nums[left],nums[right]])
                #   the second comparison condition avoids 
                #   an unnecessary run that has been done previously
                while left < right and nums[left]==nums[left+1]:
                    left+=1
                while left < right and nums[right]==nums[right-1]:
                    right-=1
                    
                left+=1
                right-=1
    return res

#no sorting version
def threeSum2(nums):
    
#nums = [-2, 0, 0, 2, 2]
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum2(nums))