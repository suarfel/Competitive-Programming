class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = '_'
                count += 1
 
        for i in range(len(nums)):
            j = i-1
            k = i
            while j >= 0 and nums[j] == '_' and nums[k] != '_': 
                nums[j] = nums[k]
                nums[k] = '_'
                k -= 1
                j -= 1
        return len(nums)-count
        