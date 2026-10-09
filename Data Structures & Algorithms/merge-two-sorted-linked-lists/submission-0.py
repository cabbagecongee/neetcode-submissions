# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        dummy = ListNode()
        curr = dummy
                
        while (head1 != None or head2 != None):
            if head1 == None:
                while head2 != None:
                    curr.next = head2
                    head2 = head2.next
                    curr = curr.next
                return dummy.next
            elif head2 == None:
                while head1 != None:
                    curr.next = head1
                    head1 = head1.next
                    curr = curr.next
                return dummy.next
            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
        return dummy.next
