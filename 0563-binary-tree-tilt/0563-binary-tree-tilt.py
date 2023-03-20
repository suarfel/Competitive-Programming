# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.nodeSum(root)
        self.tiltSum(root)
        return self.allSum(root)
    def nodeSum(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        if root:
            root.val += self.nodeSum(root.left)  + self.nodeSum(root.right)
        return root.val
    def tiltSum(self,root):
        summ = 0
        if root.left and root.right:
            root.val =  abs(root.left.val- root.right.val)
            summ += root.val
            self.tiltSum(root.left)
            self.tiltSum(root.right)
        elif root.left:
            root.val = root.left.val
            summ += root.val
            self.tiltSum(root.left)
        elif root.right:
            root.val = root.right.val
            summ += root.val
            self.tiltSum(root.right) 
        else:
            root.val = 0
            return summ
        return summ
    def allSum(self,root):
        summ = 0
        if not root:
            return 0
        if root:
            summ += abs(root.val) + abs(self.allSum(root.left)) + abs(self.allSum(root.right))
        return summ