class WordDictionary:

    def __init__(self):
        
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        
        current = self.root
        
        for char in word:
            if  current.children[ord(char) - ord('a')] == None:
                current.children[ord(char) - ord('a')] = TrieNode()
                
            
            current =  current.children[ord(char) - ord('a')]
        
        current.is_end = True
        

    def search(self, word: str) -> bool:
        
        current = self.root
        a = word
        def find(word,current):
            
            if len(word) == 0:
                return current.is_end
            
            if word[0] == '.':
                ans = False
                for i in current.children:
                    if i != None:
                        ans = False or find(word[1:],i)
                        
                        if ans:
                            return ans
                return ans
                        
            else:
                if current.children[ord(word[0]) - ord('a')] == None:
                    return False
                current = current.children[ord(word[0]) - ord('a')]
                
                return False or find(word[1:],current)
            
        return find(word,current)
                
                    

        

class TrieNode:
    
    def __init__(self):
        
        self.children = [None for _ in range(27)]
        self.is_end = False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)