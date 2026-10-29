# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def helper(node, min_v, max_v):
            if not node:
                return True
            if node.val <= min_v or node.val >= max_v:
                return False
            return helper(node.left, min_v, node.val) and helper(node.right, node.val, max_v)
        
        return helper(root, float('-inf'), float('inf'))