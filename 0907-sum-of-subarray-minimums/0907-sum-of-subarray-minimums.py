class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        sum = 0
        for i,val in enumerate(arr):
            while stack and arr[stack[-1]] > val:
                temp = stack.pop()
                right = i
                left  = stack[-1] if stack else -1
                sum += arr[temp]*(temp -left)*(right-temp)
            stack.append(i)
        l = len(stack)
        for i in range(l):
            temp = stack.pop()
            right = len(arr) 
            left = stack[-1] if stack else -1
            sum +=  arr[temp]*(temp -left)*(right-temp)
        if sum > 10**9 +7:
            return sum % (10**9 +7)
        else:
            return sum
            
        
            
        
        
        
        
        
        