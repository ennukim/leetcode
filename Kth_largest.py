#   Kth Largest Element in an Array
#   Amazon Interview


# Below is my version with 2 helper functions
def findKthLargest(nums, k):
    nums = quickSort(nums, 0, len(nums)-1)
    return nums[-k]

def quickSort(nums,start,end): 
    if start < end: 
        def part(nums, start, end):
            pivot = nums[end]
            i = start-1
            for j in range(start, end):
                if nums[j] < pivot:
                    i += 1
                    nums[j], nums[i] = nums[i], nums[j]

            nums[i+1],nums[end] = nums[end],nums[i+1] 
            return i+1
        pi = part(nums, start, end) 

        quickSort(nums, start, pi-1) 
        quickSort(nums, pi+1, end)
    return nums

nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums, k))


# Below would only work when elements don't repeat
# d = dict()
    # p = 0

    # for i in range(k):
    #     p = 0
    #     max_num = float('-inf')
    #     while p < len(nums):
    #         if nums[p] > max_num and nums[p] not in d:
    #             max_num = nums[p]
    #         p += 1
    #     d[max_num] = i

    # return max_num