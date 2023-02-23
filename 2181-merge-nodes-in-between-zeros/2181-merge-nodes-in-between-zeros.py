# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = head.next
        current = head
        new_head = ListNode()
        head = new_head
        temp = 0
        while current:
            if current.val != 0:
                temp += current.val
            else :
                new_head.next = ListNode(temp,None)
                new_head = new_head.next
                temp = 0
            current = current.next
        return head.next
        