# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        index = 0
        first = ListNode()
        even  = first
        second = ListNode()
        odd = second
        while head:
            if index % 2 == 0:
                first.next = ListNode(head.val,None)
                first = first.next
            else:
                second.next = ListNode(head.val,None)
                second = second.next
            head = head.next
            index  += 1
        odd_even_list = even
        while even:
            if even.next == None:
                even.next = odd.next
                break
            even = even.next
        return odd_even_list.next
        
                
                
            
        