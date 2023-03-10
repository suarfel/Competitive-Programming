# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        arr = self.inOrder(root)
        lst_1=[(arr.count(x),x) for x in set(arr)]
        max_count=max(lst_1)[0]
        ans = []
        for ele in lst_1:
            if ele[0]==max_count:
                ans.append(ele[1])
        return ans
    def inOrder(self,root):
        arr = []
        if root:
            arr += self.inOrder(root.left)
            arr.append(root.val)
            arr += self.inOrder(root.right)
        return arr