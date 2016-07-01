# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        copy_headA = headA
        copy_headB = headB
        firstArrival_A = True
        firstArrival_B = True
        firstMet = True
        intersection = None
        if copy_headA != None and copy_headB != None:
            while True:
                if copy_headA == copy_headB and firstMet:
                    intersection = copy_headA
                    firstMet = False
                if copy_headA.next == None and firstArrival_A == False:
                        break
                if copy_headB.next == None and firstArrival_B == False:
                        break
                if copy_headA.next == None and firstArrival_A:
                    copy_headA = headB
                    firstArrival_A = False
                    if copy_headB.next == None and firstArrival_B: 
                        copy_headB = headA
                        firstArrival_B = False
                    else:
                        copy_headB = copy_headB.next
                elif copy_headB.next == None and firstArrival_B:    
                        copy_headB = headA
                        firstArrival_B = False
                        if copy_headA.next == None and firstArrival_A:
                            copy_headA = headB
                            firstArrival_A = False
                        else:
                            copy_headA = copy_headA.next
                else:
                    copy_headA = copy_headA.next
                    copy_headB = copy_headB.next
            if intersection != None:
                return intersection
            else:
                return None
        else:
            return None
        
            
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """