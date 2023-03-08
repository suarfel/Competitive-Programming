# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        arr_order = self.inOrder(root)
        for i in range(1,len(arr_order)):
            if arr_order[i-1] >= arr_order[i]:
                return False
        return True
    def inOrder(self,root):
        arr = []
        if root:
            arr += self.inOrder(root.left)
            arr.append(root.val)
            arr += self.inOrder(root.right)
        return arr
        
            
        
        