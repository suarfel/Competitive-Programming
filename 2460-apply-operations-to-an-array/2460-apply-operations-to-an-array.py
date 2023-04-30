class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        ans = []
        arr = []
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] :
                nums[i] *= 2
                nums[i+1] = 0
            if nums[i] != 0:
                ans.append(nums[i])
            else:
                arr.append(nums[i])
        ans.append(nums[-1])
        return ans + arr
                
        