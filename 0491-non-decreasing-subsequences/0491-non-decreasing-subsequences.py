class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        arr = []
        return self.backTrack(nums,ans,arr,0)
    def backTrack(self,nums,ans,arr,idx):
        if len(arr) > 1:
            ans.append(tuple(arr))
        visited = set()
        for i in range(idx,len(nums)):
            if not arr or arr[-1] <= nums[i]:
                if nums[i] not in visited:
                    arr.append(nums[i])
                    self.backTrack(nums,ans,arr,i+1)
                    visited.add(nums[i])
                    arr.pop()
        return ans
        