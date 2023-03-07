# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left and right 
        arr  = []
        if root:
            arr +=self.inorderTraversal(root.left)
            arr.append(root.val)
            arr +=self.inorderTraversal(root.right)
        return arr
            