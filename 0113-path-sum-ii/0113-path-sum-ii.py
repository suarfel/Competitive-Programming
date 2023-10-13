# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

    
        def in_order(root,total,arr):
            
            if root.left:
                in_order(root.left,total + root.val,arr + [root.val])
            if root.right:
                in_order(root.right,total + root.val,arr + [root.val])   
            if not root.left and not root.right:
                if total + root.val  == targetSum :
                    ans.append(arr + [root.val])
                
        
        ans = []
        if not root:
            return ans
        in_order(root,0,[])
        
        return ans