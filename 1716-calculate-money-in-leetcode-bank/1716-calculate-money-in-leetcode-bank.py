class Solution:
    def totalMoney(self, n: int) -> int:
        
        constant = 1
        ans = 0
        
        while n > 0 :
            for day in range(min(7,n)):
                ans += constant + day
            
            n -= 7
            constant += 1
        return ans
        