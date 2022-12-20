# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        current = head 
        listNode = []
        while current :
            listNode.append(ListNode(current.val,None))
            current = current.next
        listNode = listNode[1:]

        while len(listNode) != 0 :
            head.next = listNode[-1]
            head = head.next
            listNode.pop(-1)
            if  len(listNode) != 0 :
                head.next = listNode[0]
                head = head.next
                listNode.pop(0)