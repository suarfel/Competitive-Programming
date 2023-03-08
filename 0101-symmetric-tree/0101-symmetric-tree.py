# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        arr_one = self.traverse_left(root.left)
        arr_two = self.traverse_right(root.right)
        print(arr_one)
        print(arr_two)
        if len(arr_one) > len(arr_two) or len(arr_one) <  len(arr_two):
            return False
        for i in range(len(arr_one)):
            if arr_one[i] != arr_two[i]:
                return False
        return True
    
    def traverse_left(self,root):
        arr = []
        if root:
            arr += self.traverse_left(root.left)
            arr.append(root.val)
            arr += self.traverse_right(root.right)
        arr.append(None)
        return arr
    
    def traverse_right(self,root):
        arr = []
        if root:
            arr += self.traverse_right(root.right)
            arr.append(root.val)
            arr += self.traverse_left(root.left) 
        arr.append(None)
        return arr
        