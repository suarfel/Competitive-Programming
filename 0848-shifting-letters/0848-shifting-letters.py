class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        pre_sum = []
        total = sum(shifts)
        pre_sum.append(total)
        
        for i in range(1,len(shifts)):
            pre_sum.append(pre_sum[i-1]-shifts[i-1])
        
        s = list(s)
        for i in range(len(s)):
            
            aski = ord(s[i]) - 97 + pre_sum[i]
            if aski > 25:
                aski = aski%26
             
            s[i] = chr(aski + 97)
            
        s = "".join(s)
        
        return s
                
                            