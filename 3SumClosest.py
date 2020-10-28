#My initial try
def threeSumClosest(nums, target):
    summed = 0
    result = 0
    closest = float('inf')
    nums.sort()
    length = len(nums)

    for i in range(length-2):
        left, right = i+1, length-1
        while left < right:
            summed = nums[i] + nums[left] + nums[right]
            diff = abs(target - summed)
            if diff < closest:
                closest = diff
                result = summed
            if summed < target:
                left+=1
            else:
                right-=1
        if closest == 0:
            break  
    return result

nums = [-1,2,1,-4]
target = 1
print(threeSumClosest(nums, target))