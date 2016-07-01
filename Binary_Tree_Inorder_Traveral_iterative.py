# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        solution = []
        stack = []
        
        while len(stack) != 0 or root != None:
            if root != None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                solution.append(root.val)
                root = root.right
            
        return solution
        
            
        
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        