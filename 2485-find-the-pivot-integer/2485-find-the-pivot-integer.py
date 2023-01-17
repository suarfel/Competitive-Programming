class Solution:
    def pivotInteger(self, n: int) -> int:
        nums = []
        for i in range(n):
            nums.append(i+1)
        for i in range(len(nums)):
            if i > 0 :
                nums[i] += nums[i-1]
        if n==1:
            return 1
        for i in range(1,len(nums)):
            if nums[i] == nums[len(nums)-1]-nums[i-1]:
                return i+1
        return -1
