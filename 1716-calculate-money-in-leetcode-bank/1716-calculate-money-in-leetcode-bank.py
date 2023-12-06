class Solution:
    def totalMoney(self, n: int) -> int:
        
        d = {1 : 1 , 2 : 2, 3 : 3, 4 : 4, 5 : 5 , 6 : 6,0: 7}
        ans = 0
        
        for day in range(1,n+1):
            ans += d[day%7]
            d[day%7] += 1
        
        return ans
        