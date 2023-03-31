class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i]-1] and nums[i] != i+1:
                    temp = nums[i]
                    nums[i] = nums[nums[i]-1]
                    nums[temp-1] = temp
        for i in range(len(nums)):
            if nums[i] != i+1:
                return [nums[i],i+1]
                
        