class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        n = len(nums)
        i = n-2
        temp = []
        while i  >= 0 :
            if nums[i] < nums[i+1]:
                break
            i -= 1
        if i >= 0:
            for j in range(n - 1, i, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
        k = len(nums)-1
        while i + 1 <  k:
            nums[i + 1], nums[k] = nums[k], nums[i + 1]
            i  += 1
            k -= 1
    