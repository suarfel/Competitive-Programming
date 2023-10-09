class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        
        i = j = 0
        
        if len(s) == 0:
            return True
        
        while i < len(s) and j < len(t):
            
            
            if s[i] == t[j] and i == len(s) -1:
                return True
            if s[i] == t[j]:
                i += 1
            j += 1
            
        return False
                
        
            
        
        
        
         