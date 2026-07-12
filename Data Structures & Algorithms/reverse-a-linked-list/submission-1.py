# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        [0,1,2,3]

        None <- 0 <- 1 <- 2 -> 3
        l = 2
        mid = 3
        r = 3
        """
        if not head:
            return 

        l = None
        mid = head 
        r = head

        while r.next:
            r = r.next
            mid.next = l
            l = mid
            mid = r

        mid.next = l
        
        return mid