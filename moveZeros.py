class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i= 0
        size = len(nums)
        while i < size:
            if nums[i] == 0:
                nums.append(0)
                nums.pop(i)
                size = size -1
            else:
                i = i+1