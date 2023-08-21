# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        index = 0
        odd,even = ListNode(0),ListNode(0)
        odd_ptr,even_ptr = odd,even
        
        while head:
            
            if index % 2 == 0:
                even_ptr.next = head
                even_ptr = even_ptr.next 
            else:
                odd_ptr.next = head
                odd_ptr = odd_ptr.next
                
            head = head.next
            index  += 1
            
        odd_ptr.next = None
        even_ptr.next = odd.next
        return even.next
 
                
            
        