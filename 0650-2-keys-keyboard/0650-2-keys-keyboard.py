class Solution:
    def minSteps(self, n: int) -> int:
        
        @lru_cache(None)
        def dp(scr,cli):
            
            if scr == n:
                return 0
            if scr > n:
                return float('inf')
            
            cp_pa = dp(scr + scr,scr) + 2
            
            pa = float('inf')
            if cli:
                pa = dp(scr + cli,cli) + 1
            
            return min(cp_pa,pa)
        
        return dp(1,0)
                        
        
                
