# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            new_node  = None
            while head :
                temp = head.next
                head.next = new_node
                new_node = head
                head = temp
            return new_node
        new_node = reverse(head)
        current = new_node
        current_max = new_node.val
        while new_node.next:
            if new_node.next.val < current_max:
                new_node.next = new_node.next.next
            else:
                new_node = new_node.next
                current_max = new_node.val
        return reverse(current)
        