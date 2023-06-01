# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
      
        def dp_rob(root):
            if root:
                left = dp_rob(root.left)  
                right = dp_rob(root.right)
                return  (root.val + left[1] + right[1],max(left)+ max(right))
            if not root:
                return (0,0)
        return max(dp_rob(root))