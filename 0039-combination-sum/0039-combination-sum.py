class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backTrack(candidate,candidate_sum,idx):
            if candidate_sum == target:
                ans.append(list(candidate))
                return 
            if len(candidates) == idx or candidate_sum > target:
                return 
            candidate.append(candidates[idx])
            backTrack(candidate,candidate_sum + candidates[idx],idx)
            candidate.pop()
            backTrack(candidate,candidate_sum,idx+1)
        backTrack([],0,0)
        return ans
            
                
                