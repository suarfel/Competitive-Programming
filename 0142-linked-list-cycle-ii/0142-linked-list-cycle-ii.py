# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_dict = {}
        while head:
            if head in node_dict:
                return head
            node_dict[head] = True
            head = head.next
        return None