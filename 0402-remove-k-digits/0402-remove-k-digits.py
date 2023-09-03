import sys
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []        
        for idx,val in enumerate(num):
            while stack and int(val) < int(stack[-1]) and k > 0:
                stack.pop()
                k -= 1
            stack.append(val)

        ans =  ''.join(stack)
        if k > 0:
            ans = ans[:-k]
        
        if not ans:
            return '0'
        sys.set_int_max_str_digits(100000)
        ans = int(ans)
        return str(ans)
        
        
        