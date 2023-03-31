class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] <= len(nums) and nums[i]>0 and nums[i] != nums[nums[i]-1]  and nums[i] != i+1 :
                temp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[temp-1] = temp
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums) + 1
    
        