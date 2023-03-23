class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = self.quickSort(nums)
        nums.reverse()
        return nums[k-1]
    def quickSort(self,nums):
        if len(nums) <= 1:
            return nums
        p = nums[0]
        l = []
        r = []
        for i in range(1,len(nums)):
            if p > nums[i]:
                l.append(nums[i])
            else:
                r.append(nums[i])
        return self.quickSort(l) + [p] + self.quickSort(r)
        
        