class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans = 0
        
        for i in left:
            ans = max(ans, abs(0 - i))
        
        for i in right:
            ans = max(ans, abs(n - i))
        
        return ans
        