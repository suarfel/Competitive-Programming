class Solution:
    def isValid(self, s: str) -> bool:
        stack1=['(','{','[']
        stack2=[]
        for i in s:
            if i in stack1:
                stack2.append(i)
            elif len(stack2)==0:
                return False
            elif i == ')' and stack2[-1]=='(':
                stack2.pop(-1)
            elif i == '}' and stack2[-1]=='{':
                stack2.pop(-1)
            elif i == ']' and stack2[-1]=='[':
                stack2.pop(-1)
            else:
                stack2.append(i)
        if len(stack2)==0:
            return True
        else:
            return False
            
                
                
                
                
        
        