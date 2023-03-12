# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        stack = []
        ans = []
        stack.append(root)
        while stack:
            head = stack.pop()
            ans.append(head.val)
            if head.right :
                stack.append(head.right)
            if head.left:
                stack.append(head.left)
        return ans