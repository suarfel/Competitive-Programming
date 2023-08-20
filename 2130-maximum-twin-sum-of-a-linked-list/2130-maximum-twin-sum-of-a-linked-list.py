# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        reverse_node = None
        fast = slow = head
        max_sum = 2
         
        while fast and fast.next:
            fast = fast.next.next
            next_node = head.next
            head.next = reverse_node
            reverse_node = head
            head = next_node

        while reverse_node and head :
            if (reverse_node.val + head.val) > max_sum:
                max_sum = reverse_node.val + head.val
            head = head.next
            reverse_node = reverse_node.next
        return max_sum


