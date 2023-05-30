class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        def dp_rob(n,arr):
            if n == 0:
                return arr[0]
            if n == 1:
                return max(arr[0],arr[1])
            if n not in memo:
                memo[n] = max(dp_rob(n-1,arr),dp_rob(n-2,arr) + arr[n])
                
            return memo[n]
        
        arr_one = nums[1:]
        arr_two = nums[:-1]
        
        if len(nums) < 3 : 
            return max(nums)
        
        
        val_one = dp_rob(len(arr_one)-1,arr_one)
        memo = {}
        val_two = dp_rob(len(arr_two)-1 ,arr_two)
        
      
        return max(val_one,val_two)
                