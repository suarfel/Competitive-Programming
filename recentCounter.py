class RecentCounter:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        

    def ping(self, t: int) -> int:
        self.queue1.append(t)
        if len(self.queue2) == 0:
            self.queue2.append(1)
        elif t-self.queue1[0] > 3000 :
            self.queue2.append(self.queue2[-1]+1)
            for i in range(len(self.queue1)-1):
                if t-self.queue1[0] > 3000:
                    self.queue2[-1] = self.queue2[-1]-1
                    self.queue1.pop(0)
        else:
            self.queue2.append(self.queue2[-1] +1)
        return self.queue2[-1]
            
        
        
        
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)