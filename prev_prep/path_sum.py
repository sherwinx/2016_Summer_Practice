# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        left = False
        right = False
        if root == None:
            return False
        if root.val == sum and root.left == None and root.right == None:
            return True
        if root.left != None:
            left = self.hasPathSum(root.left, sum - root.val)
        if root.right != None:
            right = self.hasPathSum(root.right, sum - root.val)
        return (left or right)
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        