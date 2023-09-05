class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        k_val = float('-inf')
        nums.reverse()
        
        for idx,val in enumerate(nums):
            
            if k_val > val:
                return True
    
            while stack and stack[-1] < val:
                k_val = stack.pop()
            
            stack.append(val)
        
        return False
        
        
    
                
