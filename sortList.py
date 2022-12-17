# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        listValues = []
        while head :
            listValues.append(head.val)
            head = head.next
        listValues.sort()
        if len(listValues) > 0:
            node = ListNode(listValues[0],None)
            listValues.pop(0)
        else :
            return None
        current =node
        while len(listValues) > 0:
            node.next = ListNode(listValues[0],None)
            node = node.next
            listValues.pop(0)
        return current