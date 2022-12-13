# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        node = None
        listAnswer = []
        listNodes = []
        while head :
            nextNode = head.next
            head.next = node 
            node = head
            head = nextNode
        current = node
        while current :  
            if len(listAnswer) == 0:
                listAnswer.append(0)
                listNodes.append(current.val)
                current = current.next
            elif  len(listNodes) == 0  :
                listAnswer.append(0)
                listNodes.append(current.val)
                current = current.next
            elif current.val < listNodes[-1]:
                listAnswer.append(listNodes[-1])
                listNodes.append(current.val)
                current = current.next
            elif current.val  >= listNodes[-1]:
                listNodes.pop(-1)
        listAnswer.reverse()
        return listAnswer