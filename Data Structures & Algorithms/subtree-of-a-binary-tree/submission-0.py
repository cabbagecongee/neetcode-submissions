# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def istree(self, node, subNode):
            if not node and not subNode:
                return True
            elif not node or not subNode:
                return False
            elif node.val != subNode.val:
                return False
            return (self.istree(node.left, subNode.left) and self.istree(node.right, subNode.right))
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        if self.istree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)