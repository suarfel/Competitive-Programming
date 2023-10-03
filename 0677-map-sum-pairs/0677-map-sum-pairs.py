class MapSum:

    def __init__(self):
        self.root =  TrieNode()
        self.checker = {}
        

    def insert(self, key: str, val: int) -> None:
        current = self.root
        
        if key not in self.checker:
            
            for char in key:
                
                if current.children[ord(char) - ord('a')] == None:
                    current.children[ord(char) - ord('a')] = TrieNode()
 

                current = current.children[ord(char) - ord('a')]
                current.total += val
            # current.total = val
            self.checker[key] = val
        else:
            for char in key:
                current = current.children[ord(char) - ord('a')]
                current.total -= self.checker[key]
                current.total += val
                
            # current.total -= self.checker[key]
            # current.total += val
            self.checker[key] = val

    def sum(self, prefix: str) -> int:
        current = self.root
        
        for char in prefix:
            if current.children[ord(char)-ord('a')] == None:
                return 0
            current = current.children[ord(char)-ord('a')]
            
        return  current.total
        

class TrieNode:
    
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.total = 0

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)