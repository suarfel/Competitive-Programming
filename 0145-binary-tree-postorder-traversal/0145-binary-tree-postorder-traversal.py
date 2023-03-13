# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 
        ans = []
        stack = []
        explored = set()
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root.right and root.right not in explored:
                    stack.append(root)
                    root = root.right
                else:
                    explored.add(root)
                    ans.append(root.val)
                    root = None
        return ans
            
        