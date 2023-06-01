# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @lru_cache(None)
        def dfs(node):
            
            if not node:
                return 0
            
            # pick
            pick = node.val
            if node.left:
                if node.left.left:
                    pick += dfs(node.left.left) 
                if node.left.right:
                    pick += dfs(node.left.right)
                    
            if node.right:
                if node.right.left:
                    pick += dfs(node.right.left) 
                if node.right.right:
                    pick += dfs(node.right.right)
            
            not_pick = 0
            # not pick
            if node.right:
                not_pick += dfs(node.right)
                
            if node.left:
                    
                not_pick += dfs(node.left)
                    
            return max(pick, not_pick)
       
    
        return dfs(root)
                
                
                
            
            
            
        
        
        
        
#          nonlocal ans
#             if root.left and root.right:
#                 left = dp_rob(root.left)
#                 right = dp_rob(root.right)
#                 ans = max(ans,left[1]+right[1] + root.val,left[0]+right[0])
                
#                 return (left[1]+right[1] + root.val,left[0]+right[0])
#             elif root.left :
#                 left = dp_rob(root.left)
#                 ans = max(ans,left[0] , left[1] +  root.val)
#                 return (left[1] + root.val,left[0])
#             elif root.right:
#                 right = dp_rob(root.right)
#                 ans = max(ans,right[0] , right[1] +  root.val)
#                 return (right[1] + root.val,right[0])
#             else:
#                 ans = max(ans,root.val)
#                 return (root.val,0)
        