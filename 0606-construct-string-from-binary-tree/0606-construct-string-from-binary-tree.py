# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        string = ""  
        if root:
            string += str(root.val)
            if root.left or root.right:
                string += '('
                string += self.tree2str(root.left)
                string += ')'
            if root.right:
                string += '('
                string += self.tree2str(root.right)
                string += ')'
        return string
            
            
        