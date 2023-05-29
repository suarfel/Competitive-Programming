class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def dp(target_sum):
            if target_sum > amount :
                return float('inf')
            if target_sum == amount:
                return 0
            if  target_sum not in memo:
                memo[target_sum] = float('inf')
                for coin in coins:
                    memo[target_sum] = min(memo[target_sum], dp(target_sum + coin))
                
            return memo[target_sum] + 1
        
        count = dp(0)
        if count == float('inf'):
            return -1
        return count
            