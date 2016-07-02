# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        solution = []
        if root == None:
            return solution
        level = []
        level.append(root)
        while len(level) != 0:
            solution.append([i.val for i in level])
            new_level = []
            for number in level:
                if number.left != None:
                    new_level.append(number.left)
                if number.right != None:
                    new_level.append(number.right)
            level = new_level
            
        return solution
            
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        