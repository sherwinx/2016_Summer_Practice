# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        solution = []
        if root == None:
            return solution
        solution.append(root.val)
        if root.left != None:
            solution.extend(self.preorderTraversal(root.left))
        if root.right != None:
            solution.extend(self.preorderTraversal(root.right))
        
        return solution
        """
        :type root: TreeNode
        :rtype: List[int]
        """