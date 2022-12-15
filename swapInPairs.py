# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current  = head
        listNodes = []
        listOddNodes = []
        listEvenNodes = []
        while current :
            listNodes.append(ListNode(current.val,None))
            current = current.next
        for i in range(len(listNodes)):
            if i % 2 == 0:
                listEvenNodes.append(listNodes[i])
            else:
                listOddNodes.append(listNodes[i])
        listNodes = []
        for i in range(len(listEvenNodes)):
            if len(listOddNodes) > i:
                listNodes.append(listOddNodes[i])
            listNodes.append(listEvenNodes[i])
        while len(listNodes) != 1 and head:
            listNodes[-2].next = listNodes[-1]
            listNodes.pop(-1)
            if len(listNodes) == 1:
                return listNodes[0]
        return head
