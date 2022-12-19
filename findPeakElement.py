class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        secondNums = nums
        value = max(secondNums)
        index = nums.index(value)
        return index