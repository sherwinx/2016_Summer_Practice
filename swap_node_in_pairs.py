# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        prev = None
        ans = head
        if head != None:
            if head.next != None:
                ans = head.next
        while head != None and head.next != None:
            next = head.next
            head.next = head.next.next
            next.next = head
            if prev != None:
                prev.next = next
            prev = head
            head = head.next
        return ans
        """
        :type head: ListNode
        :rtype: ListNode
        """
        