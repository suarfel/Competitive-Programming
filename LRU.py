class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheList= []
        self.cache = {}
        self.key = set()
    def get(self, key: int) -> int:
        if key in self.key :
            temp = self.cache[key]
            self.cacheList.remove([key,temp])
            self.cacheList.append([key,temp])
            return temp
        return -1  
    def put(self, key: int, value: int) -> None:
        temp = True
        if key in self.key:
            self.cacheList.remove([key,self.cache[key]] )
            self.cache[key] = value
            temp = [key,value]
            self.cacheList.append(temp)
            temp = False 
        if temp :  
            if len(self.cacheList) == self.capacity :
                current = self.cacheList[0] 
                self.key.remove(current[0])
                del self.cache[current[0]]
                self.cacheList.pop(0)
                self.key.add(key)
                self.cache[key] = value
                self.cacheList.append([key,value])
            else :
                self.key.add(key)
                self.cache[key] = value
                self.cacheList.append([key,value])
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)