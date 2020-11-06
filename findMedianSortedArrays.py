#   Median of Two Sorted Arrays 
#   Amazon Interview Question

#   Using Binary Search Algorithm
def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        return findMedianSortedArrays(nums2, nums1)

    start = 0
    end = len(nums1)
    INT_MIN = -2**64
    INT_MAX = 2**64

    while start <= end:
        x_bound = (start + end) // 2
        y_bound = (len(nums1) + len(nums2) + 1) // 2  - x_bound

        x_left = nums1[x_bound-1] if x_bound > 0 else INT_MIN
        x_right = nums1[x_bound] if x_bound < len(nums1) else INT_MAX

        y_left = nums2[y_bound-1] if y_bound > 0 else INT_MIN
        y_right = nums2[y_bound] if y_bound < len(nums2) else INT_MAX

        # pull x_bound to left
        if x_left > y_right:
            end = x_bound - 1
        # push x_bound toward right
        elif y_left > x_right:
            start = x_bound + 1
        # if correct bound
        else:
            #even
            if (len(nums1) + len(nums2)) % 2 == 0:
                return (max(x_left, y_left) + min(x_right, y_right)) / float(2)
            #odd
            else: 
                return max(x_left, y_left)

nums1 = [1,2]
nums2 =[3,4]
print(findMedianSortedArrays(nums1, nums2))