# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergeList(list_one,list_two):
            if not list_one:
                return list_two
            if not list_two:
                return list_one
            if list_one.val >= list_two.val:
                list_two.next = mergeList(list_one,list_two.next)
                return list_two
            else:
                list_one.next = mergeList(list_one.next,list_two)
                return list_one
                
        ans = None
        for i in range(len(lists)):
            ans  = mergeList(ans,lists[i])
        return ans
                
         
            
                
            
        