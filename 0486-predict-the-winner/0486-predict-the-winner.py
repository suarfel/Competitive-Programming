class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        return self.predict(0,len(nums)-1,nums) >= 0
        
    def predict(self,start,end,nums):
        if start == end:
            return nums[start]
        
        left = nums[start] - self.predict(start+1,end,nums)
        right = nums[end] - self.predict(start,end-1,nums)
        
        return max(left,right)
        
        
         
        