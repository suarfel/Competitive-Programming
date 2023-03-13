# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 
        queue = []
        ans = []
        level = 0
        queue.append((root,level))
        while queue:
            root = queue.pop(0)
            if not ans:
                ans.append([root])
            else:
                if ans[-1][-1][1] == root[1]:
                    ans[-1].append(root)
                else:
                    ans.append([root])
            if root[0].left:
                queue.append((root[0].left,root[1]+1))
            if root[0].right:
                queue.append((root[0].right,root[1]+1))
        for i in  range(len(ans)):
            for j in range(len(ans[i])):
                ans[i][j] = ans[i][j][0].val
        return ans
                
            
        
            
        
        