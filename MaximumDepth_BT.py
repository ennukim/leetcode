class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    #   My solution
    def maxDepth(self, root):
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        elif root.left is None:
            right_height = self.maxDepth(root.right)
            return 1 + right_height
        elif root.right is None:
            left_height = self.maxDepth(root.left)
            return 1 + left_height
        else:
            right_height = self.maxDepth(root.right)
            left_height = self.maxDepth(root.left)
            return 1 + max(right_height, left_height)
   
    #   leetcode solution
    def maxDepth2(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))