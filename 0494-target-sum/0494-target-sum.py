class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dp(n,target_sum):
            if n == 0 :
                if target_sum == target:
                    return 1
                else:
                    return 0
            
            key = (n,target_sum)
            if key not in memo:
                memo[key] = dp(n-1,target_sum + nums[n-1]) + dp(n-1,target_sum - nums[n-1])
            
            return memo[key]
        
        val = dp(len(nums),0)
        return val
        
        