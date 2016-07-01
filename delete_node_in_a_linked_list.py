# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
##如果这个node是在end of the list就不行，因为你call node.next 会报错

class Solution(object):
    def deleteNode(self, node):
        if node != None:
            node.val = node.next.val
            node.next = node.next.next
        return
            
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        