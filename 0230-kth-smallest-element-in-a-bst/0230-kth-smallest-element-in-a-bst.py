# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = self.inOrder(root)
        for i in range(len(arr)):
            if k == i+1:
                return arr[i]
            
    def inOrder(self,root):
        arr = []
        if root:
            arr += self.inOrder(root.left)
            arr.append(root.val)
            arr += self.inOrder(root.right)
        return arr
        