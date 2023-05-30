class Solution:
    @lru_cache(maxsize= None)
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        count = self.climbStairs(n-1) + self.climbStairs(n-2)
        return count
            
        
        
        
            
        