class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count = len(nums) + 1
        k,j = 0,0
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        while j < len(nums):
            if nums[j] < target :
                j += 1
            else:
                if j < count:
                    count = j +1
                while nums[j]-nums[k] >= target:
                    print(nums[j]-nums[k])
                    if j-k < count :
                        count = j-k
                    k += 1
                j += 1
        if count == len(nums) + 1:
            count = 0
        return count