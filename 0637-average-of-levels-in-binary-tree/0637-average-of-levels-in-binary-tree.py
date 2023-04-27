# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        ans = []
        queue = [(root,0)]
        
        while queue:
            
            root = queue.pop(0)
            print(root[0].val)
            
            if not ans :
                ans.append([root])
            else:
                if ans[-1][-1][1]  == root[1]:
                    ans[-1].append(root)
                else:
                    ans.append([root])
            if root[0].left:
                queue.append((root[0].left,root[1]+1))
            if root[0].right:
                queue.append((root[0].right,root[1]+1))
        a = []
        for i in ans:
            summ = 0
            for j in i:
                summ += j[0].val
            a.append(summ/len(i))    
        return a
                
                
                
            
            
            
            
            
            
        