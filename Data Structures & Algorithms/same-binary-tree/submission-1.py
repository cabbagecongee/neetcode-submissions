# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        curr_p = p
        curr_q = q

        def helper(t1, t2):
            if not t1 and not t2:
                return True
            elif not t1 or not t2 or (t1.val != t2.val):
                return False
            else:
                return helper(t1.left, t2.left) and helper(t1.right, t2.right)
        
        return helper(curr_p, curr_q)
        