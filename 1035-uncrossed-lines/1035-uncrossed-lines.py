class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i,j):
            
            if i < 0 or j < 0 :
                return 0
            
            if nums1[i] == nums2[j] :
                return 1 + dp(i -1,j-1)
            else:
                return max(dp(i,j-1),dp(i-1,j))
            
        
        return dp(len(nums1)-1,len(nums2)-1)
            