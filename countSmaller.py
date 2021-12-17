class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        newNums = [0]*len(nums)
        for i in range(len(nums)):
            counter = 0 
            for j in range(len(nums)):
                if i != j and nums[i] > nums[j]:
                    counter += 1
            newNums[i] = counter
        return newNums
        