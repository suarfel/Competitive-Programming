# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len = 0
        point= 0
        temp =head
        while head:
            len = len +1
            head= head.next
        len = len//2 +1
        while temp:
            point+=1
            if point == len:
                return temp
            temp =temp.next