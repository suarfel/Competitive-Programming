class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []
        
        for element in s:
            
            if not stack:
                stack.append((element,1))
            elif stack[-1][0] == element and stack[-1][1] == k-1:
                for i in range(k-1):
                    stack.pop()
            elif stack[-1][0] == element:
                stack.append((element,stack[-1][1]+1))
            else:
                stack.append((element,1))
        arr = [ele[0] for ele in stack]     
        ans = ''.join(arr)
        
        return ans
                
                
                
                
        