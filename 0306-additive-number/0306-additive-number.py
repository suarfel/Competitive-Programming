class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        if len(num) < 3:
            return False
        ans = []
        
        def back_track(start):
            
            if len(ans) > 2:
                if int(ans[-3]) + int(ans[-2]) == int(ans[-1]):
                    ans_num = "".join(ans)
                    if len(ans_num) == len(num):
                        return True
                else:
                    return 
                
            for end in range(start,len(num)):
                
                if num[start:end+1][0] != '0' or (num[start:end+1][0] == '0' and len(num[start:end+1]) == 1) :
                    ans.append(num[start:end+1])
                    temp = back_track(end + 1)
                    
                    if temp:
                        return True
                    ans.pop()

        valid = back_track(0)
        
        if valid:
            return valid
        return  False
        
        
            
            
            
            
                
                
                
                
        
        