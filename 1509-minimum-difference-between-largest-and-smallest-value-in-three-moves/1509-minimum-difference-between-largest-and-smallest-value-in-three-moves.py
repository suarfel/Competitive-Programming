class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        nums.sort()
        if len(nums) < 5 :
            return 0
        min_change = float('inf')
        min_change = min(min_change,nums[len(nums)-4]-nums[0])
        min_change = min(min_change,nums[len(nums)-3]-nums[1])
        min_change = min(min_change,nums[len(nums)-2]-nums[2])
        min_change = min(min_change,nums[len(nums)-1]-nums[3])
        return min_change
    
                        
                    
                
                
           
                
        
            
        