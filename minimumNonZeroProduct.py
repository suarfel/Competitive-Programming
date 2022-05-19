class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        x = pow(2,p) - 1
        x*(pow(x-1,x//2))

        


sol =Solution()
sol.minNonZeroProduct(2)
 