class Solution:
    def longestWord(self, words: List[str]) -> str:
        self.root = TrieNode()
        
        for word in words:
            self.insert(word)
        ans = ""
        for i in range(len(words)):
            
            valid = True
            for j in range(1,len(words[i])+1):
                valid = valid and self.search(words[i][:j])
            if valid:
                if len(words[i]) > len(ans):
                    ans = words[i]
                elif len(words[i]) == len(ans):
                    ans = min(ans,words[i])
                    
        return ans
    
        
    def insert(self,word):
        
        current = self.root
        
        for char in word:
            
            if current.children[ord(char) -ord('a')] == None:
                current.children[ord(char) - ord('a')] = TrieNode()
            
            current = current.children[ord(char) -ord('a')]
        
        current.is_end = True
        
    def search(self,word):
        
        current = self.root
        
        for char in word:
            
            if current.children[ord(char) -ord('a')] == None:
                return False
            
            current = current.children[ord(char) -ord('a')]
        
        return current.is_end
        
    
class TrieNode:
    
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False