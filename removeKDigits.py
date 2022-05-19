class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if (k == len(num)):
            return "0"
        
        stack = []
        stack.append(num[0])
        i = 1
        while i < len(num) and k > 0:
            if len(stack)>0 and int(num[i]) < int(stack[-1]):                    
                stack.pop()    
                k -= 1
            else:
                stack.append(num[i])
                i += 1
        
        finalnum = "".join(stack)  
        finalnum += num[i:]
        
        if k>0:
            finalnum = finalnum[:-k]
        
        return self.remzeros(finalnum)
    
    def remzeros(self, s):
        if (len(s)==0):
            return '0'
        while (s[0]=='0'):
            s = s[1:]
            if (len(s)==0):
                return '0'
        
        return s
            
        