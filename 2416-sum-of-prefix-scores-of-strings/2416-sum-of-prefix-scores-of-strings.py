class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        self.root = TrieNode()
        
        for char in words:
            self.insert(char)
        
        ans = []
        for char in words:
            ans.append(self.search(char))
            
        return ans
    def insert(self,word):
        
        current = self.root
        
        for char in word:
            
            if current.children[ord(char) - ord('a')] == None:
                current.children[ord(char) - ord('a')] = TrieNode()
                
            
            current = current.children[ord(char) - ord('a')]
            current.count += 1
        
    def search(self,word):
        ans = 0
        current = self.root
        
        for char in word:
            current = current.children[ord(char) - ord('a')]
            ans += current.count
            
        return ans
class TrieNode:
    def __init__(self):
        
        self.children = [None for i in range(26)]
        self.count = 0
        
        