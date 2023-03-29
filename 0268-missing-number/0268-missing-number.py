class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            while  nums[i] < len(nums) and nums[i] != i:
                temp = nums[i]
                nums[i] = nums[nums[i]]
                nums[temp] = temp
        for i in range(len(nums)-1):
            if nums[i+1]  < nums[i]:
                return i
            elif nums[i+1] - nums[i] == 2:
                return nums[i] +1
        if len(nums) == nums[-1]:
            return 0
        return len(nums)
