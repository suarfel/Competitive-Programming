class MyLinkedList:
    def __init__(self):
        self.head = None 
    def get(self, index: int) -> int:
        counter = 0
        temp = self.head
        while temp:
            if counter == index :
                return temp.val
            elif counter > index :
                return -1
            else :
                temp = temp.next
                counter += 1
        return -1
    def addAtHead(self, val: int) -> None:
        temp= ListNode(val,None)
        temp.next = self.head
        self.head = temp
    def addAtTail(self, val: int) -> None:
        temp = self.head
        current = ListNode(val,None)
        if temp is None:
            self.head = current
        while temp:
            if temp.next  == None:
                temp.next = current
                break
            else :
                temp = temp.next
    def addAtIndex(self, index: int, val: int) -> None:
        counter = 0
        if self.head is None and index == 0:
            self.head = ListNode(val,None)
        temp = self.head
        while temp:
            if index == 0 :
                current = ListNode(val,None)
                current.next = temp
                self.head = current
                break 
            elif counter == index-1 :
                nextNode = temp.next
                current =ListNode(val,None)
                current.next = nextNode
                temp.next = current
                
                break
            elif counter > index:
                break
            else :
                temp = temp.next
                counter += 1
       
    def deleteAtIndex(self, index: int) -> None:
        counter = 0
        temp = self.head
        while temp:
            if index == 0 :
                temp = temp.next
                self.head = temp
                break
            elif counter == index-1 :
                if temp.next != None :
                    nextNode = temp.next.next
                    temp.next =  nextNode
                else :
                    break
                break 
            elif counter > index:
                break   
            else :
                temp = temp.next
                counter += 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)