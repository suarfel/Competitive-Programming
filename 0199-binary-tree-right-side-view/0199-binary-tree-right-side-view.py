# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 
        queue = []
        level = 0
        arr = []
        queue.append((root,level))
        while queue:
            root = queue.pop(0)
            if not arr:
                arr.append([root])
            else:
                if arr[-1][-1][1] == root[1]:
                    arr[-1].append(root)
                else:
                    arr.append([root])
            if root[0].right:
                queue.append((root[0].right,root[1]+1))
            if root[0].left:
                queue.append((root[0].left,root[1]+1))
        ans = []
        for i in range(len(arr)):
            ans.append(arr[i][0][0].val)
        return ans
            
        
            
        