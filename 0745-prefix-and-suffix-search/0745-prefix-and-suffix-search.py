class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        
        for idx,word in enumerate(words):
            
            temp_word = word[::-1]
            for i in range(len(word)):
                self.insert(word[i:]+"{"+word,idx)
        
    def insert(self,word,real):
        
        current = self.root
        for char in word:
            
            if current.children[ord(char) - ord('a')] == None :
                current.children[ord(char) - ord('a')] = TrieNode()
            current = current.children[ord(char) - ord('a')] 
            
            if real > current.largest:
                current.largest = real
    

    def f(self, pref: str, suff: str) -> int:
        search = suff + "{" + pref
        current = self.root
        
        for char in search:
            if current.children[ord(char) - ord('a')] == None:
                return -1
            current = current.children[ord(char) - ord('a')]
            
        return current.largest
            
class TrieNode:
    
    def __init__(self):
        
        self.children = [None for _  in range(27)]
        self.largest = -1
        
            
            
            
        
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)



