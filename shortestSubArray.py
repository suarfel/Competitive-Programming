class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int: 
        indicator =1
        i=0
        while i < len(nums):
            for j in range(len(nums)):
                a =sum(nums[j:j+indicator])
                if a >= k:
                    return i + 1
                elif a < k and i == len(nums)-1:
                    return -1 
            indicator += 1 
            i += 1