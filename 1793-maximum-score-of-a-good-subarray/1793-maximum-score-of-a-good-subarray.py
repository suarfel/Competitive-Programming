class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        nums.append(float('-inf'))
        max_score = 0
        stack = []
        for idx,val in enumerate(nums):
            while stack and nums[stack[-1]] >= val:
                temp = stack.pop()
                left = stack[-1] if stack else -1
                right = idx
                if left < k < right:
                    score = nums[temp]*(right-left-1)
                    if score > max_score:
                        max_score = score
            stack.append(idx)
        return max_score
        
        
        
        
        
        
         
        
        
        
        
        