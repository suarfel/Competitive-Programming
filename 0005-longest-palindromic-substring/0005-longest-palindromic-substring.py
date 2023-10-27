class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = 0
        right = 0
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                left = i
                right = i + 1
        
        for diff in range(2,n):
            
            for i in range(n-diff):
                
                j = i + diff
                
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    left = i
                    right = j
        
        return s[left:right+1]
        
        
            
            
            
            
            
            
            
        