def search(nums, target):
    start = 0
    end = len(nums)-1

    while start <= end:
        mid = (start + end) // 2
        if target == nums[mid]:
            return mid
        elif nums[mid] >= nums[start]:
            if target >= nums[start] and target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target <= nums[end] and target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1

    if nums[mid] != target:
        return -1
    return mid

nums = [1,2,3]
target = 1
print(search(nums, target))