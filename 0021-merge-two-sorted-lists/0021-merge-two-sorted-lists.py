# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        merged_list = temp
        def sort(lis1,lis2,temp):
            if lis1 is None or lis2 is None:
                if lis1 is None:
                    temp.next = lis2
                    return temp
                else:
                    temp.next = lis1
                    return temp
            else:
                if lis1.val < lis2.val :
                    temp.next = lis1
                    lis1 = lis1.next
                else :
                    temp.next = lis2
                    lis2 = lis2.next
                temp = temp.next
                sort(lis1,lis2,temp)    
        sort(list1,list2,temp)
        return merged_list.next

