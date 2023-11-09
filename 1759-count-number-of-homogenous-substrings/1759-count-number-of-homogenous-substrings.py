class Solution:
    def countHomogenous(self, s: str) -> int:
        
        ans = 0
        count = 1
        
        for idx in range(1,len(s)):
            
            if s[idx] == s[idx-1]:
                count += 1
            else:
                ans += (count*(count + 1))//2
                count = 1
                
        ans += (count*(count + 1))//2
                
        return ans % (pow(10,9) + 7 )
            
            
        
        
        
        
        