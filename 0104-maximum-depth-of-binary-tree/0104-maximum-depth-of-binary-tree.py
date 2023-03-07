# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        counter = 0
        counter_two = 0
        if root:
            counter += self.maxDepth(root.left)
            counter += 1
            counter_two += self.maxDepth(root.right)
            counter_two += 1
        return max(counter,counter_two)
            
            