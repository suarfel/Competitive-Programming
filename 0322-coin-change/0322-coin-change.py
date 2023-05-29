class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @lru_cache(maxsize = None)
        def dp(target_sum):
            if target_sum > amount :
                return float('inf')
            if target_sum == amount:
                return 0
            
            _min = float('inf')
            for coin in coins:
                _min = min(_min,dp(target_sum + coin))
                
            return 1 + _min
        
        count = dp(0)
        if count == float('inf'):
            return -1
        return count
            