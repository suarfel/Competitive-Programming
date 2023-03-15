class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = str(n)
        arr = [int(i) for i in nums]
        idx = float("inf")
        final = 0
        l = 0
        for i in range(len(arr)-2,-1,-1):
            if arr[i] < arr[i+1]:
                idx = i
                break
        if idx == float('inf'):
            return -1
        for i in range(idx+1,len(nums)):
            if arr[idx] < arr[i] :
                final = i
            else:
                break
        num_one = ''.join(nums[0:idx]) + nums[final]
        num_two = nums[idx] + nums[idx+1:final] + ''.join(nums[final+1:]) 
        num_three = [int(i) for i in num_two]
        num_three.sort()
        num_three = [str(i) for i in num_three]
        ans  = int(num_one + ''.join(num_three))
        if ans > 2**31 - 1:
            return -1
        return ans