# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        left = False
        right = False
        if p and q :
            if p.val == q.val:
                left = self.isSameTree(p.left,q.left)
                right = self.isSameTree(p.right,q.right)
            else:
                return False
        elif p and not q:
            return False
        elif q and not p:
            return False
        else:
            return True
        return left and right 
                    
            
                
                
        