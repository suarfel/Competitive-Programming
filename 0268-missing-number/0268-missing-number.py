class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] > 1:
                return nums[i] - 1
        if len(nums) == nums[-1]:
            return 0
        else:
            return nums[-1] + 1
        