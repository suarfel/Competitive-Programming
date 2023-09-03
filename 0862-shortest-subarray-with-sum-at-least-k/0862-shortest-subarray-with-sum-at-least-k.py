class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        queue = deque()
        
        if len(nums) == 1:
            if k == nums[0]:
                return 1
            else:
                return -1
            
        pre_fix = [0]
        
        for i in range(len(nums)):
            pre_fix.append(pre_fix[-1]+nums[i])
            
        min_size = float('inf')
        
        for idx,val in enumerate(pre_fix):
            
            while queue and val <= pre_fix[queue[-1]]:
                queue.pop()
            
            while queue and val- pre_fix[queue[0]] >= k:
                min_size = min(min_size,idx - queue.popleft())
            
            queue.append(idx)
    
        if min_size == float('inf'):
            return -1
        
        return min_size
                
            
            
                
            
                
            
            
            
        
            
            
        