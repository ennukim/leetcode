#Using Hashmap 
#Hashmap - space O(n)
#Time - O(n)
def missingNumber(nums):
    nums_dict = dict()

    #you may use set(nums) instead of dict() for less lines
    for i in range(len(nums)):
        if nums[i] not in nums_dict:
            nums_dict[nums[i]] = None
        else:
            pass

    for i in range(len(nums)+1):
        if i not in nums_dict:
            return (i)
        else:
            pass

#leetcode version of using bitmap
#time comp - O(n)
#space - O(1)
def missingNumber2(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing


nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))
