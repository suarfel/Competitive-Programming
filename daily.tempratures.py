class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans =[0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:  
                element = stack.pop()
                ans[element] = i - element
            stack.append(i)                    
        return ans