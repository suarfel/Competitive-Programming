# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        listNodes = []
        while head:
            listNodes.append(ListNode(head.val,None))
            head = head.next 
        for i in range(1,len(listNodes)):
            temp = listNodes[i]
            k = i
            while k > 0 and temp.val < listNodes[k-1].val:
                listNodes[k] = listNodes[k-1]
                k -= 1
            listNodes[k] = temp
        current = listNodes[0]
        while len(listNodes) != 1:
            while  listNodes[0] :
                if listNodes[0].next == None :
                    listNodes[0].next = listNodes[1]
                    break
                listNodes[0] = listNodes[0].next
            listNodes.pop(1)
        return  current