class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        ans = set()
        
        def valid_parenthese(s):
            
            character_dict = {"(" : ")"}
            stack = []
            
            for i in s:
                if i in character_dict:
                    stack.append(i)
                else:
                    if stack and character_dict[stack[-1]] == i:
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0
        
        
        def back_track(idx,temp):
            
            if len(temp) == n*2:
                if valid_parenthese(temp):
                    ans.add(temp)
                return 
        
            for i in range(2):
                
                if i == 0:
                    temp += "("
                else:
                    temp += ')'
                  
                back_track(idx + 1,temp)
                temp = temp[:len(temp)-1]
                 

        back_track(0,"")
        return list(ans)
                
                
                
                
                
                