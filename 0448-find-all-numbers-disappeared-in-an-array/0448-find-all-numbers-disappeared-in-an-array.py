class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)
        nums = set(nums)
        ans = []
        for i in range(l):
            if i+1 not in nums:
                ans.append(i+1)
        return ans
        
                
        