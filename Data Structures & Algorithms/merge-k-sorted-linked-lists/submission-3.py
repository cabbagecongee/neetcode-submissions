# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
            
        # prev = ListNode()
        # head = prev
        # curr = None

        # for l in lists:
        #     curr = l
        #     prev.next = curr

        #     while curr.next:
        #         curr = curr.next
        #     prev = curr
        
        # return head.next
        
        vals = []
        for l in lists:
            curr = l
            while curr:
                vals.append(curr.val)
                curr  = curr.next
        
        vals.sort()
        head = ListNode()
        curr = head
        for v in vals:
            curr.next = ListNode(v, None)
            curr = curr.next
        
        return head.next
            
        