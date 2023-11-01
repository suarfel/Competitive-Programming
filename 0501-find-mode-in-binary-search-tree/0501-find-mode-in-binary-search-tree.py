# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        d = defaultdict(int)
        
        def mode(root):
            
            if not root:
                return 
            d[root.val] += 1
            mode(root.left)
            mode(root.right)
            
        mode(root)
        sorted_dict = dict(sorted(d.items() , key=lambda item : item[1],reverse = True))
        
        temp = float('-inf')
        ans = []

        for key in sorted_dict:
            if temp > sorted_dict[key]:
                return ans
            else:
                temp = sorted_dict[key]
                ans.append(key)
                
        return ans
            
            