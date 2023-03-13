# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 
        counter = 0
        arr = self.inOrder(root)
        for i in arr:
            temp = []
            temp = list(self.inOrderValues(i))
            if temp[0] == sum(temp)//len(temp):
                counter += 1
        return counter
    def inOrder(self,root):
        ans = []
        if root:
            ans += self.inOrder(root.left)
            ans.append(root)
            ans += self.inOrder(root.right)
        return ans
    def inOrderValues(self,root):
        ans = []
        if root:
            ans.append(root.val)
            ans += self.inOrderValues(root.left)
            ans += self.inOrderValues(root.right)
        return ans
            
        
            
        