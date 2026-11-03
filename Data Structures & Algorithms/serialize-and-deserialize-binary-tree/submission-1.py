# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.tree = ""
        def serialize_helper(node): # dfs
            if node:
                self.tree += "," + str(node.val)
                serialize_helper(node.left)
                serialize_helper(node.right)
            else:
                self.tree += ",null"
        
        serialize_helper(root)
        if self.tree != "":
            return self.tree[1:]
        return self.tree
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]: # must use dfs here
        def deserialize_helper():
            node = next(nodes)
            if node != "null":
                curr = TreeNode(int(node))
                curr.left = deserialize_helper()
                curr.right = deserialize_helper()
                return curr
            else:
                return None

        nodes = iter(data.split(","))
        curr = None
        
        return deserialize_helper()
        
