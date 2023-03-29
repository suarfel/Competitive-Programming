class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            count = 0
            while i >= 2:
                if i%2 == 1:
                    count += 1
                i //= 2
            if i == 1:
                ans.append(count+1)
            else:
                ans.append(count)
        return ans
                
            
        