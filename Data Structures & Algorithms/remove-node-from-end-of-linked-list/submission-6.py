# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        l = 1
        curr = head
        while curr.next:
            l += 1
            curr = curr.next
        
        idx = l - n
        prev = ListNode()
        res = prev
        curr = head

        while curr.next and idx > 0:
            prev.next = curr
            prev = curr
            curr = curr.next
            idx -= 1
        
        if curr.next and idx == 0:
            prev.next = curr.next
        else:
            prev.next = None
        return res.next
        

        
        

