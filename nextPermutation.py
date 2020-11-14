#   Next Permutation
#   Google Interview

def nextPermutation(nums):
    orig = nums

    for i in range(len(nums)-1, 0, -1):
        if orig[i] > orig[i-1]:
            nums[i], nums[i-1] = nums[i-1], nums[i]
            return nums
    return sorted(nums)

nums = [1,2,2,1]
print(nextPermutation(nums))