class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        moves = 0
        nums.sort()
        i = 1
        while i < len(nums):
            if nums[i-1] >= nums[i]:
                moves += nums[i-1] - nums[i] + 1
                nums[i] += nums[i-1] - nums[i] + 1 
            i += 1
        return moves
                
        