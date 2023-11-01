class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        count = 0
        unique_counter = defaultdict(int)
        
        for idx,val in enumerate(nums):
            unique_counter[val] += 1
        
        for idx,val in enumerate(nums):
            
            if unique_counter[val] > 0:
                unique_counter[val] -= 1
            else:
                continue
            if k - val in unique_counter and unique_counter[k-val] > 0 :
                count += 1
                
                unique_counter[k-val] -= 1
                
                
        return count
            