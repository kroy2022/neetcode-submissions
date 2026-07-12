# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        """
        p1, p2 = list1, list2
        newList = ListNode() 
        head = newList

        while p1 and p2:
            if p1.val <= p2.val:
                newList.next = p1
                p1 = p1.next
            else:
                newList.next = p2
                p2 = p2.next
            
            newList = newList.next
        
        while p1:
            newList.next = p1
            p1 = p1.next
            newList = newList.next
        
        while p2: 
            newList.next = p2
            p2 = p2.next
            newList = newList.next
        
        return head.next