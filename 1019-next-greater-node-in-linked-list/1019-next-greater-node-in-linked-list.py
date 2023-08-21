# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        ans = []
        current = head
        
        while current:
            ans.append(0)
            current = current.next
        i = 0
        
        while head:
            while stack and stack[-1][1] < head.val:
                idx,val = stack.pop()
                ans[idx] = head.val
            
            stack.append((i,head.val))
            head = head.next
            i += 1
        
        return ans
            



