# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        stack = []
        used = set()
        solution = []
        if root != None:
            stack.append(root)
            
        while len(stack) != 0:
            p = stack.pop()
            if p in used:
                solution.append(p.val)
            else:
                used.add(p)
                stack.append(p)
                if p.right != None:
                    stack.append(p.right)
                if p.left != None:
                    stack.append(p.left)
        
        return solution
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        