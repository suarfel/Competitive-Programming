# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        step = 0
        nodeList = []
        current = head 
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
                nodeList.append(ListNode(head.val,None))
                nodeList.append(head.next)
                break 
            
            nodeList.append(ListNode(head.val,None))
            head = head.next
        for i in range(len(nodeList)-1):
            nodeList[-(i+2)].next = nodeList[-(i+1)]
             
        return nodeList[0]