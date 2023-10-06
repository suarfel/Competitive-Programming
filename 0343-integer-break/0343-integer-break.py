class Solution:
    def integerBreak(self, n: int) -> int:
        
        ans = 1
        cm = n
        
        while n > 4:
            ans *= 3
            n -= 3
        
        
        if cm > 4 or n == 4:
            ans *= n
        else:
            ans *= (n-1)
            
        return ans