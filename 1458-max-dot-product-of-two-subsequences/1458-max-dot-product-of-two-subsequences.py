class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i,j):
            
            if i == len(nums1)or j == len(nums2) :
                return float('-inf')
            
            return max(nums1[i]*nums2[j] + max(dp(i+1,j+1),0),dp(i+1,j),dp(i,j+1))
        
        return dp(0,0)