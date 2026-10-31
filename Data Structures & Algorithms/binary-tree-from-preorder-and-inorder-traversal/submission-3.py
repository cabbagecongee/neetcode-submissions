# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        inorder_idx = {val: i for i, val, in enumerate(inorder)}

        def recurse(min_idx, max_idx, pre_idx):
            if (min_idx == max_idx) or pre_idx > len(preorder) - 1:
                return None
            if (min_idx == max_idx - 1):
                return TreeNode(inorder[min_idx])
            in_root = None
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            mid = inorder_idx[root_val]
            root.left = recurse(min_idx, mid, pre_idx+1)
            root.right = recurse(mid+1, max_idx, pre_idx + (mid - min_idx) + 1)
            return root
        
        root = recurse(0, len(preorder), 0)
        return root
        

