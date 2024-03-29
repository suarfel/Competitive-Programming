# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root,number):
            if root:
                number += str(root.val)
                if root.left  and root.right :
                    dfs(root.left,number)
                    dfs(root.right,number)
                elif root.left:
                    dfs(root.left,number)
                else:
                    dfs(root.right,number)
            else:
                self.ans += int(number)
                number = number[:len(number)-1]
            return self.ans
      
        return dfs(root,'')
        