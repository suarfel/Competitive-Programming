
class Trie:

    def __init__(self):
        
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        
        current = self.root
        
        for char in word :
            
            if current.children[ord(char) - ord('a')] == None:
                
                current.children[ord(char) - ord('a')] = TrieNode()
                
            current =  current.children[ord(char) - ord('a')]
            
        current.is_end = True
                

    def search(self, word: str) -> bool:
        
        current = self.root
        
        for char in word :
            
            if current.children[ord(char) - ord('a')] == None:
                return False
                
            current =  current.children[ord(char) - ord('a')]
            
        if current.is_end:
            return True
        else:
            return False
            
    def startsWith(self, prefix: str) -> bool:
        
        current = self.root
        
        for char in prefix :
            
            if current.children[ord(char) - ord('a')] == None:
                return False
                
            current =  current.children[ord(char) - ord('a')]
            
        return True
        
        

class TrieNode:
    
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)