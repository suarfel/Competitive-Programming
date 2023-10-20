class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        
        count = 0
        ans = nums[0]
        for num in nums:
            ans &= num
            
        temp = nums[0]
        total = 0
        for i in range(len(nums)):
            temp &= nums[i]
            
            if temp == ans:
                
                count += 1
                total += temp
                temp = pow(2,20)-1
                
        if ans == total :
            return count
        return 1
                
                
                
            
        
        