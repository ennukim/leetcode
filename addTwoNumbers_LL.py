class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(l1, l2):
        header = ListNode(0)
        trailer = header # same LN however, the pointer is different.
        quotient = 0

        while l1 or l2:
            val = quotient
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            
            remainder = val % 10
            quotient = val // 10
            
            new_node = ListNode(remainder)
            trailer.next = new_node #  
            trailer = trailer.next #   trailer is a node, so it has to be updated with a new node
            
        if quotient > 0:
            trailer.next = ListNode(quotient)

        return header.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.next.next.next = None

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = None

l3 = (Solution.addTwoNumbers(l1, l2))

cursor = l3
while(cursor != None):
    print(cursor.val)
    cursor = cursor.next