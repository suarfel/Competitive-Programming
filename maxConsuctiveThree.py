class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxNumber = 0
        tempMax = 0
        flip = 0
        i = 0
        j = 0 
        while j < (len(nums)):
            if nums[j] == 1:
                tempMax += 1
                if tempMax > maxNumber:
                    maxNumber = tempMax
                j += 1
            else:
                if flip < k :
                    tempMax += 1
                    if tempMax > maxNumber :
                        maxNumber = tempMax
                    flip += 1
                    j += 1
                else:
                    if nums[i] == 0 :
                        flip -= 1
                        tempMax -= 1 
                        i += 1
                    else :
                        tempMax -= 1 
                        i += 1
        return maxNumber