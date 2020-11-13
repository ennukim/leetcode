#   Missing Ranges
#   Linear Scan Alogrithm (Many Edge Cases)
#   Google Interview Question

def findMissingRanges(nums, lower, upper):
    ans = []
    left = 0
    right = 1

    if len(nums) == 0:
        if lower == upper:
            return [str(lower)]
        else:
            return [str(lower) + "->" + str(upper)]
    else:
        if abs(nums[0] - lower) > 0:
            if  nums[0] - lower == 1:
                ans.append(str(lower))
            else:
                ans.append(str(lower)+"->"+str(nums[0]-1))

        while (right < len(nums)):
            if nums[right] - nums[left] > 0:
                if nums[right] - nums[left] == 1:
                    left += 1
                    right += 1
                elif nums[right] - nums[left] == 2:
                    ans.append(str(nums[left]+1))
                    left += 1
                    right += 1
                else:
                    ans.append(str(nums[left]+1)+"->"+str(nums[right]-1))
                    left += 1
                    right += 1

        if abs(upper - nums[len(nums)-1]) > 0:
            if upper - nums[len(nums)-1] == 1:
                ans.append(str(upper))
            else:
                ans.append(str(nums[len(nums)-1]+1)+"->"+str(upper))

    return ans

# nums = [0,1,3,50,75]
# lower = 0
# upper = 99

# nums = []
# lower = -3
# upper = -1

nums = [-1]
lower = -2
upper = -1

# nums = [9]
# lower = 0
# upper = 9

print(findMissingRanges(nums, lower, upper))
