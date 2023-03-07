# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        elif root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                node = root.right
                while node.left:
                    node = node.left
                root.val = node.val
                root.right = self.deleteNode(root.right,node.val)
        return root
            
            
            