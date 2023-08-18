# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        temp_node = ListNode(0)
        revers_node = temp_node
        temp_node_two = ListNode(0)
        actual_node = temp_node_two
        temp_node_two.next = head
        current = head
        count = 1
        
        while count <= right:
            if count == left :
                temp_node_two.next = None
                while left <= right :
                    temp_node.next = current
                    temp_node = temp_node.next
                    current = current.next
                    left += 1
                temp_node.next = None
                break
            else:
                current = current.next
                temp_node_two = temp_node_two.next
                count += 1
                
        node = None
        revers_node = revers_node.next
        
        while  revers_node:
            next_node = revers_node.next
            revers_node.next = node
            node = revers_node
            revers_node = next_node
        temp_node_two.next = node
        while temp_node_two.next:
            temp_node_two = temp_node_two.next
        temp_node_two.next = current
        return actual_node.next
        
        
        
        
        
        
        