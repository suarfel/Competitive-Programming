class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            while nums[i] != nums[nums[i]-1] and nums[i] != i+1:
                temp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[temp-1] = temp
        for i in range(len(nums)):
            if nums[i] != i+1:
                ans.append(nums[i])
        return ans
        