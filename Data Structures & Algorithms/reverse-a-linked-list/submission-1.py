# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        n = head
        prev = None
        while n:
            future = n.next
            n.next = prev
            prev = n
            n = future

        return prev


            


