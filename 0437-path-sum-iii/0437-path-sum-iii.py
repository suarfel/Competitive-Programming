# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.pathCount = 0
        self.treeSum(root,targetSum)
        return self.pathCount
    def treeSum(self,root,targetSum):
        if not root:
            return
        else:
            self.eachNode(root,targetSum,0)
            self.treeSum(root.left,targetSum)
            self.treeSum(root.right,targetSum)
    def eachNode(self,root,targetSum,sum):
        if not root:
            return
        sum += root.val
        if sum == targetSum:
            self.pathCount += 1
        self.eachNode(root.left,targetSum,sum)
        self.eachNode(root.right,targetSum,sum)
        
        
        
        
        
        
        
                