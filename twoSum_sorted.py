#   Two Sum II - Input array is sorted
#   Amazon Interview Question


def twoSum(numbers, target):
    left = 0
    right = len(numbers)-1
    
    while left < right:
        summed = numbers[left] + numbers[right]
        if summed == target:
            return left+1, right+1
        elif summed < target:
            left += 1
        elif summed > target:
            right -= 1
            

numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))