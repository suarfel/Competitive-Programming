class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        for i in range(len(nums)):
            if i == 0:
                if nums[-1] - nums[0] == 0:
                    return i
            elif i == len(nums)-1 :
                if nums[i-1] == 0:
                    return i
            else :
                if nums[i-1] == nums[-1] - nums[i]:
                    return i
        return -1