class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans = float('-inf')
        temp = 0 
        left = 0
        
        while left < len(nums):
            temp += nums[left]
            if temp  > 0 or temp > ans:
                ans = max(ans,temp)
            if temp < 0 :
                temp = 0
            left += 1
            
                
        return ans
            
            
            
            
            
        