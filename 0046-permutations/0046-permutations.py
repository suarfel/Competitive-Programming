class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        return self.backTrack(nums,temp,ans,0)
    def backTrack(self,nums,temp,ans,bm):
        if len(nums) == len(temp):
            ans.append(temp.copy())
        for i in range(len(nums)):
            if not (bm & 1 << i):
                temp.append(nums[i])
                bm |= 1<<i
                self.backTrack(nums,temp,ans,bm)
                bm ^= 1<<i
                temp.pop()
        return ans