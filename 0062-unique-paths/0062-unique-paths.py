class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}
        
        def dp(m,n):
            if m < 0 or n < 0:
                return 0
            if m == 0 and n == 0:
                return 1
            
            key = (m,n)
            if key not in memo:
                memo[key] = dp(m-1,n) + dp(m,n-1)
            
            return memo[key]
        return dp(m-1,n-1)
        