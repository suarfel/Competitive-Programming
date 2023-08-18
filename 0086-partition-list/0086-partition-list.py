# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        less,greater = ListNode(0),ListNode(0)
        less_ptr,greater_ptr = less,greater
        
        while head:
            if head.val < x:
                less_ptr.next = head
                less_ptr = head
            else:
                greater_ptr.next = head
                greater_ptr = head
            head = head.next
            
        greater_ptr.next = None
        less_ptr.next = greater.next
        
        return less.next
        
                
                
                
                
                
            
        