# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None :
            return list2
        elif list2 is None:
            return list1
        if list1.val <= list2.val:
            head = ListNode(list1.val,None)
            temp = head 
            list1 = list1.next
        else : 
            head = ListNode(list2.val,None)
            temp = head 
            list2 = list2.next 
        print(temp)
        while list1 or list2 :
            print(temp)
            if list1 is None:
                head.next = list2
                return temp
            elif list2 is None:
                head.next = list1
                return temp
            if  list1.val <= list2.val   :
                head.next = ListNode(list1.val,None)
                head = head.next
                list1 = list1.next
            else : 
                head.next = ListNode(list2.val,None) 
                head = head.next
                list2 = list2.next 