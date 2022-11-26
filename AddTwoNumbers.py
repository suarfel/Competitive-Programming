# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(0,None)
        current = ListNode(0,None)
        nodeList = []
        list1 = []
        list2 = []
        str1 = ''
        str2 = ''
        print(l1)
        while l1 != None :
            list1.append(l1.val)
            l1 = l1.next 
        while l2 != None :
            list2.append(l2.val)
            l2 = l2.next
        for i in range(len(list1)):
            str1 = str1 + str(list1[-(i+1)])
        for i in range(len(list2)):
            str2 = str2 + str(list2[-(i+1)])
        for i in str(int(str1) + int(str2)):
            nodeList.append(ListNode(i,None))
        
        for i in range(len(nodeList)-1):
            nodeList[-(i+1)].next = nodeList[-(i+2)]

        return nodeList[-1]