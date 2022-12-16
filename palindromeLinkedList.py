# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = ListNode(head.val,None)
        orignal = temp
        current = head.next
        while current:
            temp.next = ListNode(current.val,None)
            temp  = temp.next
            current =  current.next
        node = None
        while orignal :
            nextNode = orignal.next
            orignal.next = node
            node = orignal
            orignal = nextNode
        while head:
            if head.val == node.val :
                node = node.next
                head = head.next
            else :
                return False
        return True