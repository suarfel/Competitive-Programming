class Solution:
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}
        def costCalculate(n):
            if n < 2 :
                return 0
            if n not in memo:
                memo[n] =  min(costCalculate(n-1)+cost[n-1],cost[n-2]+costCalculate(n-2))
            return memo[n]
        val = costCalculate(len(cost))
        return  val
         
        
        
        
        