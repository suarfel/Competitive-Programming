# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        d = defaultdict(int)
        stack = [root]
        
        while stack:
            
            last = stack.pop()
            d[last.val] += 1
            
            if last.left:
                stack.append(last.left)
            if last.right:
                stack.append(last.right)
                
        max_freq = max(d.values())
        ans = []
        
        for key in d:
            if max_freq == d[key] :
                ans.append(key)
        
        return ans
                
            
        
            
            