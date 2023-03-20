class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        print(candidates)
        def backTrack(arr,temp_sum,idx):
            if temp_sum == target:
                ans.append(tuple(arr))
                return 
            if idx == len(candidates) or target < temp_sum :
                return
            for i in range(idx,len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                arr.append(candidates[i])
                backTrack(arr,temp_sum + candidates[i],i+1)
                arr.pop()
                
                
        backTrack([],0,0)
        return  ans
            