# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def isValid(root):
            
            if not root:
                return 
            isValid(root.left)
            ans.append(root.val)
            isValid(root.right)
        
        ans = []
        isValid(root)
       
        for i in range(1,len(ans)):
            if ans[i] <= ans[i-1] :
                return False
            
        return True
    
        
        
            