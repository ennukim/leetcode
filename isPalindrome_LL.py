class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(head):
        
n2 = ListNode(2)
l1 = ListNode(1, n2)

n6 = ListNode(1)
n5 = ListNode(2, n6)
n4 = ListNode(2, n5)
l2 = ListNode(1, n4)

print(Solution.isPalindrome(l1)