class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        
        def expand(i,j):
            
            while i >= 0 and j < len(s) and s[i] == s[j]:
                
                i -= 1
                j += 1
                
            return s[i+1:j]
        
        for i in range(len(s)):
            
            ans = max(ans,expand(i,i),expand(i,i+1),key=len)
        
        return ans
            
            