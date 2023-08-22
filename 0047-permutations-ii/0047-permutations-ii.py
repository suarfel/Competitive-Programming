class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        
        def back_track(nums,arr):
            
            if not nums:
                arr = tuple(arr)
                if arr not in ans:
                    ans.append(tuple(arr))
                return
            
            for i in range(len(nums)):
                arr.append(nums[i])
                back_track(nums[:i] + nums[i+1:],arr)
                arr.pop()
  
            return ans
        
        return back_track(nums,[])
                