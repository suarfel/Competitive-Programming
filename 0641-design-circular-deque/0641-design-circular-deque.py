class MyCircularDeque:

    def __init__(self, k: int):
        self.k=k 
        self.queue =[]
    def insertFront(self, value: int) -> bool:
        temp=[]
        if len(self.queue) < self.k:
            temp.append(value)
            for i in self.queue:
                temp.append(i)
            print(temp)
            self.queue =temp
            return True
        else:
            return False
            
    def insertLast(self, value: int) -> bool:
        if len(self.queue)< self.k:
            self.queue.append(value)
            return True
        else:
            return False
        

    def deleteFront(self) -> bool:
        if len(self.queue)>=1:
            self.queue.pop(0)
            return True
        else:
            return False
              
        
    def deleteLast(self) -> bool:
        
        if len(self.queue)>=1:
            self.queue.pop(-1)
            return True
        else:
            return False
        
        

    def getFront(self) -> int:
        print(self.queue)
        if len(self.queue)>=1:
            return self.queue[0]
        else:
            return -1
        
        

    def getRear(self) -> int:
         if len(self.queue)>=1:
            return self.queue[-1]
         else:
            return -1
        
        

    def isEmpty(self) -> bool:
        if len(self.queue)==0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        print(self.queue)
        if len(self.queue)==self.k:
            return True
        else:
            return False
   
 


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()