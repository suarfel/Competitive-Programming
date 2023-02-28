# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def revere_linkedList(head):
            node = None
            while head:
                temp = head.next
                head.next = node
                node = head
                head = temp
            return node
        head_one = revere_linkedList(l1)
        head_two = revere_linkedList(l2)
        temp = ListNode()
        head = temp
        remainder = 0
        while head_one or head_two:
            sum = 0
            sum += remainder
            if head_one and head_two:
                sum += head_one.val + head_two.val
                if sum == 10:
                    temp.next = ListNode(0,None)
                    remainder = 1
                elif sum > 10:
                    temp.next = ListNode(sum%10,None)
                    remainder = sum//10
                else:
                    temp.next = ListNode(sum,None)
                    remainder = 0
                print(sum)
                head_one = head_one.next
                head_two = head_two.next
            elif head_one:
                sum += head_one.val
                print(sum)
                if sum == 10:
                    temp.next = ListNode(0,None)
                    remainder = 1
                else:
                    temp.next = ListNode(sum,None)
                    remainder = 0
                head_one = head_one.next
            else:
                sum += head_two.val
                if sum == 10:
                    temp.next = ListNode(0,None)
                    remainder = 1
                else:
                    temp.next = ListNode(sum,None)
                    remainder = 0
                head_two = head_two.next
              
            if head_one is None and head_two is None:
                temp = temp.next
                if remainder >0:
                    temp.next = ListNode(1,None)
            temp = temp.next
        head = head.next
        head = revere_linkedList(head)
        return head