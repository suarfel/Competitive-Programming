class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        arr = []
        return  self.backTrack(candidates,target,ans,arr,0) 
    def backTrack(self,candidates,target,ans,arr,idx):
        if target < 0:
            return 
        if target == 0:
            ans.append(list(arr))
        for i in range(idx,len(candidates)):
            arr.append(candidates[i])
            self.backTrack(candidates,target-candidates[i],ans,arr,i)
            arr.pop()
        return ans