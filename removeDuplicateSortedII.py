# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None :
            return head
        elif head.next:
            current = head.next
        else : 
            return head
        values = set()
        temp = head
        while current :
            if current.val == head.val:
                values.add(current.val)
                current = current.next 
            else :
                head.next = current
                head = head.next
                current = current.next
        listVal = []
        while temp:
            if temp.val in values:
                temp = temp.next
            else :
                listVal.append(ListNode(temp.val,None))
                temp = temp.next
        while len(listVal) > 1:
            listVal[-2].next = listVal[-1]
            listVal.pop(-1)
        if len(listVal) > 0:
            temp = listVal[0]
        return  temp