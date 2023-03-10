class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub_sets = []
        sub = []
        return self.backTrack(nums,sub_sets,sub,0)
    def backTrack(self,nums,sub_sets,sub,index):
        sub_sets.append(list(sub))
        for i in range(index,len(nums)):
            sub.append(nums[i])
            self.backTrack(nums,sub_sets,sub,i+1)
            sub.pop()
        return sub_sets
            
        