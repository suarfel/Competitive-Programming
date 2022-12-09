# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        countNodes = 0
        listNodes = []
        while current:
            countNodes += 1
            current = current.next
        for i in range(countNodes // k):
            node = None
            for i in range(k):
                nextNode = head.next
                head.next = node
                node = head
                head  = nextNode
            listNodes.append(node)  
        listNodes.append(head)
        current = listNodes[0]
        while len(listNodes) > 1:
            while len(listNodes)>1 :
                if listNodes[0].next == None:
                    listNodes[0].next = listNodes[1]
                    listNodes.pop(1)
                listNodes[0] = listNodes[0].next
        return current
