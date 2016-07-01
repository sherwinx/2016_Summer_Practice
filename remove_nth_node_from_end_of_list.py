# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = head
        for i in range(n - 1):
            second = second.next
        while second.next != None:
            first = first.next
            second = second.next
        first.next = first.next.next
        return dummy.next
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        