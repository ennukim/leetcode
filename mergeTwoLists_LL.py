class ListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# pointer zig zag
class Solution(object):
    def mergeTwoLists(l1, l2):
        result = cur = ListNode()
        while l1 != None and l2 != None: #l1 and l2 both have to be not None
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next #l1 is replaced here
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return result.next

l1 = ListNode()
l1.val = 1
l1.next = ListNode()
l1.next.val = 2
l1.next.next = ListNode()
l1.next.next.val = 4

l2 = ListNode()
l2.val = 1
l2.next = ListNode()
l2.next.val = 3
l2.next.next = ListNode()
l2.next.next.val = 4
l2.next.next.next = ListNode()
l2.next.next.next.val = 5

l3 = (Solution.mergeTwoLists(l1, l2))

cursor = l3
while(cursor != None):
    print(cursor.val)
    cursor = cursor.next
