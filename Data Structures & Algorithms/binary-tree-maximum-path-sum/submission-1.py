# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # dist(root) = max{dist(left) + left.val, dist(right) + right.val} 
        self.curr_max = float('-inf')
        def dist(curr):
            sum_path = 0
            both = False
            left_max = 0
            right_max = 0
            if not curr.right and not curr.left:
                sum_path = curr.val
            elif not curr.right:
                left_max = max(dist(curr.left),0)
                sum_path = curr.val + left_max
            elif not curr.left:
                right_max = max(dist(curr.right),0)
                sum_path = curr.val + right_max
            else:
                left_max = max(dist(curr.left),0)
                right_max = max(dist(curr.right),0)
                sum_path = curr.val + left_max + right_max
                both = True
            if sum_path > self.curr_max: 
                self.curr_max = sum_path
            if not both:
                return sum_path
            else:
                return curr.val + max(left_max, right_max)
        dist(root)
        return self.curr_max
