# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        counter = 0
        temp_one = head
        temp_two = head
        temp_three = head
        while temp_one:
            counter += 1
            temp_one = temp_one.next
        if counter == 0:
            return None
        if k == 0:
            return head
        k = k % counter
        if k == 0:
            return head
        counter -= k
        while temp_two:
            if counter == 1:
                temp = temp_two.next
                temp_two.next = None
                break
            counter -= 1
            temp_two = temp_two.next
        head = temp
        while temp:
            if temp.next is None:
                temp.next =  temp_three
                break
            temp = temp.next
        return head