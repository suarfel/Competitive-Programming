# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = head
        size = 0
        while current:
            current = current.next
            size += 1
        if size%2 == 0 :
            size = size//2 -1
        else :
            size = size//2-1
        counter = 0
        while previous:
            if counter == size:
                previous.next = previous.next.next
                return head 
            else:
                previous = previous.next
            counter += 1
                
        