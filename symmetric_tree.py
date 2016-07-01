# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if root == None:
            return True
        else:
            return self.isSymmetricHelper(root.left, root.right)
    
    def isSymmetricHelper(self, leftNode, rightNode): 
        if leftNode == None:
            return rightNode == None
        if rightNode == None:
            return leftNode == None
        if leftNode.val != rightNode.val:
            return False
        if not self.isSymmetricHelper(leftNode.right, rightNode.left):
            return False
        if not self.isSymmetricHelper(leftNode.left, rightNode.right):
            return False
        else:
            return True
            
#    def isSymmetricHelper(self, leftNode, rightNode):
#        if leftNode == None and rightNode == None:
#            return True
#        elif leftNode != None and rightNode != None and leftNode.val == rightNode.val:
#            if self.isSymmetricHelper(leftNode.right, rightNode.left) and self.isSymmetricHelper(leftNode.left, rightNode.right):
#                return True
#        return False
        """
        :type root: TreeNode
        :rtype: bool
        """