# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def count(root):
            nonlocal ans
            if not root:
                return (0,0)

            left = count(root.left)
            right = count(root.right)
            
            if (left[0] + right[0] + root.val)//( left[1] + right[1] + 1) == root.val:
                ans += 1
            return (left[0] + right[0] + root.val, left[1] + right[1] + 1)
        
        count(root)
        return ans
        
            
        
            
        