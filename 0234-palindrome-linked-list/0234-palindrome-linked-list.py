# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = ListNode(0)
        orignal = temp
        current = head
        
        while current:
            temp.next =  current
            temp  = temp.next
            current =  current.next
            
        temp.next = None
        node = None
        orignal = orignal.next
        
        while head and head.next :
            head = head.next.next
            nextNode = orignal.next
            orignal.next = node
            node = orignal
            orignal = nextNode
        
        if head:
            orignal = orignal.next
        
        while orignal and node:
            if orignal.val == node.val :
                node = node.next
                orignal = orignal.next
            else :
                return False
            
        if orignal == None and node == None :
            return True
        return False