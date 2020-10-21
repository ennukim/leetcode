class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        l3 = cur = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next      
        cur.next = l1 or l2
        return l3.next

n3 = ListNode(4)
n2 = ListNode(2, n3)
l1 = ListNode(8, n2)

n5 = ListNode(4)
n4 = ListNode(3, n5)
l2 = ListNode(1, n4)

r1 = ListNode()
r2 = ListNode()

print(Solution.mergeTwoLists(l1, l2))
