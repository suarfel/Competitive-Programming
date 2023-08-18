# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        current = head
        dummy_node = ListNode("a",None)
        ans_node = dummy_node
        
        while current:
            if current.val < x:
                dummy_node.next= ListNode(current.val,None)
                dummy_node = dummy_node.next
            current = current.next
            
        
        current = head
        
        while current:
            if current.val >= x:
                dummy_node.next = ListNode(current.val,None)
                dummy_node = dummy_node.next
            current = current.next
            
        
        return ans_node.next
            
                
                
                
                
                
            
        