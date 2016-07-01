# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        ans = head
        while ans != None and ans.next != None:
            if ans.val == ans.next.val:
                ans.next = ans.next.next
            else:
                ans = ans.next
        return head
                
        """
        :type head: ListNode
        :rtype: ListNode
        """
        