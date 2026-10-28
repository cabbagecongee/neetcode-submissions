# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        traverse = []
        traverse.append([root.val])

        def helpme(node, curr_idx):

            if not node:
                return None
            if len(traverse)-1 < curr_idx:
                traverse.append([])
            if node.left:
                traverse[curr_idx].append(node.left.val)
            if node.right:
                traverse[curr_idx].append(node.right.val)
            helpme(node.left, curr_idx+1)
            helpme(node.right, curr_idx+1)
            return None
        
        helpme(root, 1)
        return traverse[:-1]


