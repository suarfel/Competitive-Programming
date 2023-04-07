class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        arr = [0]*33
        for i in range(len(nums)):
            for j in range(32):
                if nums[i] & 1<<j:
                    arr[j] += 1
        for i in range(len(arr)):
            if arr[i]%3 != 0:
                ans |= 1<<i
        if ans & 1<<31:
            return (ans - 2**32) 
        return ans 