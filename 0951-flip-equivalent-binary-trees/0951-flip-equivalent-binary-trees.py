# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
         
            
        if root1 and root2:
            if root1.val == root2.val :
                val1 = self.flipEquiv(root1.left,root2.left)
                val2 = self.flipEquiv(root1.right,root2.right)

                val3 = self.flipEquiv(root1.left,root2.right)
                val4 = self.flipEquiv(root1.right,root2.left)

                return (val1 and val2) or (val3 and val4)
            else :
                return False
        if root1 == None and root2 == None:
            return True

        else:
            return False

            