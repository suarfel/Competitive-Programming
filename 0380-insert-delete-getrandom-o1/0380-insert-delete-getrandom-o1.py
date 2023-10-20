class RandomizedSet:

    def __init__(self):
        
        self.random = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        
        if val in self.random:
            return False
        else:
            self.arr.append(val)
            self.random[val] = len(self.arr)-1
            
            return True
        

    def remove(self, val: int) -> bool:
        
        if val in self.random:
            idx = self.random[val]
            self.arr[idx] ,self.arr[len(self.arr)-1] = self.arr[len(self.arr)-1] , self.arr[idx]
            self.random[self.arr[idx]] = idx
            del self.random[self.arr[len(self.arr)-1]]
            self.arr.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        
        return random.choice(self.arr)
        
    


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()