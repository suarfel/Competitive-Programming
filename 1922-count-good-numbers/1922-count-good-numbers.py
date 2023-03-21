class Solution:
    def countGoodNumbers(self, n: int) -> int:
        x = n//2
        y = n - x
        return (pow(5,y,1000_000_007)*pow(4,x,1000_000_007))%1000_000_007
        