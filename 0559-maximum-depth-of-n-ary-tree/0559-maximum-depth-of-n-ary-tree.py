"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        count = 0
        self.ans = 0
        
        def dfs(root,count):
            count += 1
            if not root.children:
                if self.ans <= count:
                    self.ans = count
            for r in root.children:
                dfs(r,count)
        dfs(root,count)
        return self.ans
        
                
            
        