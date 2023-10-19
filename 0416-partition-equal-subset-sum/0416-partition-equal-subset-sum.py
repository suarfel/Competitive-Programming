class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        @lru_cache(None)
        def dp(n,target_sum):
            
            if n >= len(nums) or target_sum <= 0:
                return target_sum == 0
            
            return dp(n+1,target_sum-nums[n]) or dp(n+1,target_sum)
              
        return sum(nums)%2 == 0 and dp(0,sum(nums)//2)
            
        
        