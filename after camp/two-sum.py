class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # map the every in number with its index
        num_idx = {}
        
        for idx,val in enumerate(nums):
            num_idx[val] = idx
            
        for idx,num in enumerate(nums):
            if target - num in num_idx and idx != num_idx[target-num]:
                return [idx,num_idx[target-num]]
            
            
        
        
     

