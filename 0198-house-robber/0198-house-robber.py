class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        
        def dp_rob(n):
            if n == 0:
                return nums[0]
            if n == 1:
                return max(nums[0],nums[1])
            if n not in memo:
                memo[n] = max(dp_rob(n-1),dp_rob(n-2)+nums[n])
            return memo[n]
        
        return dp_rob(len(nums)-1)