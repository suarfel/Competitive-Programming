class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        pair_counter = 0
        
        for num in nums:
            pair_counter += counter[num]
            counter[num] += 1
                    
        return pair_counter 
        
        
                
        