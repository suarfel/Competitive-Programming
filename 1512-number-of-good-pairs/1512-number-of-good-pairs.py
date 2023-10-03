class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        pair_counter = 0
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    pair_counter += 1
                    
        return pair_counter 
        
        
                
        