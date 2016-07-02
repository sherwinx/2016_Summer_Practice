# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        dummy = ListNode(0)
        while head:
            next = head.next
            head.next = dummy.next
            dummy.next = head
            head = next
        return dummy.next
"""    
    def reverseList(self, head):
        return self.reverseHelper(head, None)
        
    def reverseHelper(self, head, newHead):
        if head == None:
            return newHead
        next = head.next
        head.next = newHead
        return self.reverseHelper(next, head
            
        """
        