class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        sum = 0
        for i in range(k):
            nums[0] = -nums[0]
            nums.sort()
        for i in nums:
            sum += i
        return sum