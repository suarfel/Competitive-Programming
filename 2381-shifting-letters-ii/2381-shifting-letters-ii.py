class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        shift_counter = [0 for _ in range(len(s)+1)]
        print(shift_counter)
        
        for start,end,direction in shifts:
            
            if not direction:
                direction = -1
            
            shift_counter[start] += direction
            shift_counter[end +1] -= direction
            
        for i in range(1,len(shift_counter)-1):
            shift_counter[i] = shift_counter[i-1] + shift_counter[i]
            
        s = list(s) 
        for i in range(len(s)):
            
            askii = ord(s[i]) - 97 + shift_counter[i]
            
            if askii > 25 or askii < 0:
                askii = askii%26
            
            s[i] = chr(askii + 97)
        
        s = "".join(s)
        return s
            
                
            
        
        
        
        
        