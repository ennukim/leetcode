def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    d = {}
        
    for elem in nums:
        if elem not in d:
            d[elem] = 1
        else:
            d[elem] += 1
    
    for key, value in d.items():
        if value == 1:
            return key
        else:
            pass

nums = [4,3,4,5,5]
print(singleNumber(nums))

# better space
# nums.sort()
#         i = 0
#         while len(nums) != 1:
#             if nums[i] == nums[i+1]:
#                 del nums[i:i+2]
#             else:
#                 i += 1
#         return nums[0]

# better run time
# a = 0
# for n in nums:
    
#     a ^= n
    
# return a