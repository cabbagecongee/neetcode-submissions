# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None

        def count_help(node, count):
            if node:
                count += 1
                left = count_help(node.left, 0)
                right = count_help(node.right, 0)
                return left + right + count
            return count
        
        left_count = count_help(root.left, 0)

        
        def pain(node, k):
            left_count = count_help(node.left, 0)
            if k == left_count + 1:
                return node.val
            if k <= left_count:
                return pain(node.left, k)
            elif k > left_count + 1:
                return pain(node.right, k - (left_count + 1))
        
        return pain(root, k)
            
            

