class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        arr = []
        @lru_cache(None)
        def dp(idx):
            
            if idx < 0:
                return 0
            
           
            temp = max(nums[idx],nums[idx] + dp(idx-1))
            arr.append(temp)
            return temp
        
        dp(len(nums)-1)
        return max(arr)
            

            
            
            
            
            
        