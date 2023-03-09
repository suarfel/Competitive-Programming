class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        return self.backTrack(nums,temp,ans)
    def backTrack(self,nums,temp,ans):
        if not nums:
            ans.append(temp.copy())
        else:
            for i in range(len(nums)):
                temp.append(nums[i])
                self.backTrack(nums[:i]+ nums[i+1:],temp,ans)
                temp.pop()
        return ans
            
        