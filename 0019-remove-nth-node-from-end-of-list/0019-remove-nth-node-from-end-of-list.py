# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        step = 0
        current = head 
        temp = head
        while current != None :
            count += 1
            current = current.next
        constant = count - n
        if constant == 0 :
            return head.next
        while  head:
            step += 1
            if step == constant:
                head.next = head.next.next
                break 
            head = head.next
        return temp
     


           



        