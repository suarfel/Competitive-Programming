class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        
        ans = 0
        min_ = min(nums)
        max_ = max(nums)
        
        if max_ - min_ <= k*2:
            return 0
        else:
            return max_-min_ - k*2
            
        
        
         