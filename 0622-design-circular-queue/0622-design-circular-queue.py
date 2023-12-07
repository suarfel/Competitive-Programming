class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [0]*k
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            # print(value,False)
            return False
        if self.rear == self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.front] = value
        else:
            self.queue[(self.rear+1)%self.size] = value
            self.rear = (self.rear+1)%self.size
        
        # print(self.rear,self.front)
            
        return True
            

    def deQueue(self) -> bool:
        if self.isEmpty() :
            return False
        if self.rear == self.front :
            self.front = self.rear = -1
        else:
            self.front = (self.front+1)%self.size
        return True
            
    def Front(self) -> int:
        if self.front != -1 :
            return self.queue[self.front]
        return -1
        
    def Rear(self) -> int:
        if self.rear != -1 :
            return self.queue[self.rear]
        return -1

    def isEmpty(self) -> bool:
        return  self.front == -1
    
    def isFull(self) -> bool:
        if self.front == 0 and self.rear == self.size-1:
            return True
        if self.front - self.rear == 1 :
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()