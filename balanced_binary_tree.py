# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        return self.isBalancedHelper(root) >= 0
        
    def isBalancedHelper(self, root):
        if root == None:
            return 0
        left = self.isBalancedHelper(root.left)
        right = self.isBalancedHelper(root.right)
        if left < 0 or right < 0 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
        """
        :type root: TreeNode
        :rtype: bool
        """
        