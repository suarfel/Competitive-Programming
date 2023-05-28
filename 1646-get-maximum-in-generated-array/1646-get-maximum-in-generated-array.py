class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        memo = {}
        self.dp(n,memo)
        return max(memo.values())
    
    def dp(self,n,memo):
        if n == 0:
            memo[0] = 0
            return 0
        if n == 1:
            memo[1] = 1
            return 1
        if n not in memo:
            for i in range(n,-1,-1):
                if i%2 == 0:
                    memo[i] = self.dp(i//2,memo) 
                else:
                    memo[i] = self.dp((i-1)//2,memo) +  self.dp((i-1)//2 + 1,memo)
        return memo[n]