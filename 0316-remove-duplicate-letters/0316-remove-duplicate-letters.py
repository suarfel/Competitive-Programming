class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = {}
        visited = set()
        stack = []
        
        for i,val in enumerate(s):
            counter[val] = i
             
                
        for i,val in enumerate(s):
            if val not in visited:
                while stack and val < stack[-1] and i < counter[stack[-1]]:
                    visited.remove(stack[-1])
                    stack.pop()

                stack.append(val)
                visited.add(val)
            
        print(stack)
        return ''.join(stack)
        