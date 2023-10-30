class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average = 0
        temp = 0
        j = 0
        for i in range(len(nums)):
            temp += nums[i]
            while i-j+1 == k:
                if max_average == 0 or max_average < temp/k:
                    max_average = temp/k
                temp -= nums[j]
                j +=1
        return max_average
                
        