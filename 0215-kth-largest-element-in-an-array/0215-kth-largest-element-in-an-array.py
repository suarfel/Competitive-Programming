class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = self.quickSort(nums,k)
        return nums
        # nums.reverse()
        # return nums[k-1]
    def quickSort(self,nums,k):
        if len(nums) <= 1:
            return nums[0]
        p = nums[0]
        l = []
        r = []
        for i in range(1,len(nums)):
            if p > nums[i]:
                l.append(nums[i])
            else:
                r.append(nums[i])
        if k == len(r) +1:
            return p
        elif k < len(r) +1:
            num = self.quickSort(r,k)
            return num
        else:
            num = self.quickSort(l,k-len(r)-1)
            return num
            
        
        