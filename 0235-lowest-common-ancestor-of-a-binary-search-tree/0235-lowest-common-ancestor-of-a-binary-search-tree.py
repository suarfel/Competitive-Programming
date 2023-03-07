# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root.val > p.val and root.val < q.val) or (root.val < p.val and root.val > q.val):
            return root
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root
        # elif root.val > p.val and root.
#         arr_one = self.traversal(root,p)
#         arr_two = self.traversal(root,q)
        
#         print(arr_one)
#         print(arr_two)
#         return arr_one[0]
#     def traversal(self,root,p):
#         arr = []
#         if root.val > p.val:
#             arr.append(root)
#             arr += self.traversal(root.left,p)
#             print(True)
#         elif root.val < p.val:
#             arr.append(root)
#             arr += self.traversal(root.right,p)
#         else:
#             arr.append(root)
#         return arr
#     # def isNear(self, p):
#     # self.distToPoint(p)