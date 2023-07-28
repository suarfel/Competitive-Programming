class Solution:
    def isValid(self, s: str) -> bool:
        character_dict = {"(" : ")","{" : "}","[" : "]"}
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
                