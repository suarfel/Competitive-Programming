class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = self.backTrack(nums,[],0,0)
        maxV = 1
        d = {}
        for i in ans:
            if maxV < i:
                maxV =i
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        return d[maxV]
                
    def backTrack(self,nums,ans,temp,index):
        if temp != 0:
            ans.append(temp)
        for i in range(index,len(nums)):
            self.backTrack(nums,ans,temp | nums[i],i+1)
        return ans
    
