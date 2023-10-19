# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
            
        def inOrder(root):
            if root:
                inOrder(root.left)
                arr.append(root.val)
                inOrder(root.right)
        
        arr = []
        inOrder(root)
        for i in range(len(arr)):
            if k == i+1:
                return arr[i]
        