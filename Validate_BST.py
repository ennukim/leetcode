class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root, low_range=float('-inf'), high_range=float('inf')):
        # print(root.val)
        if not root:
            return True
        elif not low_range < root.val < high_range:
            return False
        return (self.isValidBST(root.left, low_range, root.val) and self.isValidBST(root.right, root.val, high_range))