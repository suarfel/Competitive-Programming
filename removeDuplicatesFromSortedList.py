# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        temp = ListNode()
        temp.val = head.val
        head = head.next
        current = temp
        while head:
            if temp.val == head.val:
                if head.next is None:
                    return current
                head = head.next
            else :
                temp.next = ListNode(head.val,None)
                temp = temp.next
                head = head.next
        return current
            