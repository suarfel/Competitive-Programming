class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []
        for i in range(len(s)):
            
            if s[i] == '(':
                stack.append(s[i])
                
            elif s[i] == ')' and stack[-1] == '(':
                stack.pop()
                stack.append(1)
                
            else:
                counter = 0
                while stack[-1] != '(':
                    counter += stack.pop()
                    
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(counter*2)
                    
        return sum(stack)
                    
                    
                
            
                
            
            
            
                
                
                
        
        
                
        




            
        
        