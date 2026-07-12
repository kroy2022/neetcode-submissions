# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        None <- 0 -> 1 -> 2 -> 3

        p1 = 0
        p2 = 1
        temp = 2
        """
        p1 = None
        p2 = head
        
        while p2:
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp
        
        return p1
