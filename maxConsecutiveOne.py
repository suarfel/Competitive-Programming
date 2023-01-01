class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNumber = 0
        tempMax = 0
        for i in nums:
            if i == 1:
                tempMax += 1
                if tempMax > maxNumber :
                    maxNumber = tempMax
            else:
                tempMax = 0
        return maxNumber