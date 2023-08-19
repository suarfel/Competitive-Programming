# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count = 0
        while head and count <= pow(10,4):
            head = head.next
            count += 1
        if count == pow(10,4) + 1:
            return True
        return False
            