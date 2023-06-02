class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        max_val = 0
        memo = defaultdict(int)
        def dp(n,take):
            
            if n == len(prices):
                return 0
            
            state = (n,take)
            if state not in memo:
                
                memo[state] = dp(n+1,take)
            
                if take :
                    memo[state] = max(memo[state],dp(n+1,False) - prices[n])
                else:
                    memo[state] = max(memo[state],dp(n+1,True) + prices[n] - fee)
                
            return memo[state]
        
        return dp(0,True)
                
        