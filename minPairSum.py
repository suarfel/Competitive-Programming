class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        li =[]
        j = -1
        nums.sort()
        temp = len(nums)
        for i in range(temp//2):
            li.append(nums[i] + nums[j])
            j += -1
        li.sort()
        return li[-1]
        