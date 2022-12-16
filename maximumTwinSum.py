# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = ListNode(head.val,None)
        current = head.next
        orignal = temp
        maxSum = 1
        node = None
        while current :
            temp.next = ListNode(current.val,None)
            temp = temp.next
            current = current.next
        
        while orignal:
            nextNode = orignal.next
            orignal.next = node
            node = orignal
            orignal = nextNode
        while head :
            if (head.val + node.val) > maxSum:
                maxSum = head.val + node.val
                head = head.next
                node = node.next
            else :
                head = head.next
                node = node.next
        return maxSum