class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = { '2': 'abc','3' : 'def', '4':'ghi', '5':'jkl','6':'mno','7':'pqrs','8': 'tuv','9' : 'wxyz'}
        ans = []
        if not digits:
            return []
        def backTrack(st,num):
            
            if len(digits) == len(st):
                ans.append(''.join(st))
                return 
            
            if num == len(digits):
                return
            
            for i in d[digits[num]]:
                st.append(i)
                backTrack(st,num+1)
                st.pop()   
                
        backTrack([],0)
        return ans
        