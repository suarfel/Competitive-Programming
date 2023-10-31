# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
         
       
        def delete_node(root,prev):
            
            if not root :
                return 

            delete_node(root.left,root)
            delete_node(root.right,root)
            
            if root.val in to_delete:
                if root.left :
                    ans.append(root.left)
                if root.right:
                    ans.append(root.right)
                    
                if prev != None:
                    if prev.left != None and prev.left.val in to_delete:
                        prev.left = None
                    elif prev.right != None and prev.right.val in to_delete:
                        prev.right = None
                
    
           
        
        ans = []
        
        to_delete = set(to_delete)
        
        if root.val not in to_delete:
            ans = [root]
        else:
            ans = []
        
        
            
        delete_node(root,None)
        
        return ans
                
                
                
        