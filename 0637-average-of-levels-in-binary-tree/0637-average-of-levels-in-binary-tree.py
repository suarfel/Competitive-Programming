# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        ans = []
        queue = deque([root])
        
        while queue:
            
            s = 0
            length = len(queue)
            
            for i in range(len(queue)):
                node = queue.popleft()
                s += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(s/length)
           
        return ans
                
                
                
            
            
            
            
            
            
        