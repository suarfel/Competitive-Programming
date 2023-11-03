# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
    
        if not preorder: return None
        bst = TreeNode(preorder[0])
        smaller = []
        bigger = []
        for n in preorder:
            if n > preorder[0]: bigger.append(n)
            elif n < preorder[0]: smaller.append(n)
        bst.left = self.bstFromPreorder(smaller)
        bst.right = self.bstFromPreorder(bigger)
        return bst
            
                
        
            
         
        
        