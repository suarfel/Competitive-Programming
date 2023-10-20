class RandomizedCollection:

    def __init__(self):
        
        self.random = {}
        self.arr = []       

    def insert(self, val: int) -> bool:
        
        if val in self.random:
            self.arr.append(val)
            self.random[val].add(len(self.arr)-1)
            
            return False
        
        self.arr.append(val)
        self.random[val] = {len(self.arr)-1}
         
        return True
        

    def remove(self, val: int) -> bool:
        
        if val in self.random:
            
            idx = 0
            for i in self.random[val] :
                idx = i
                break
                
            self.random[val].remove(idx)
            
            if idx != len(self.arr) -1:
                self.arr[idx],self.arr[len(self.arr)-1] = self.arr[len(self.arr)-1] , self.arr[idx]
                self.random[self.arr[idx]].remove(len(self.arr)-1)
                self.random[self.arr[idx]].add(idx)
                
            self.arr.pop()
            
            if len(self.random[val]) == 0:
                del self.random[val]
            return True 
        
        return False
        
        

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()