import datetime 
class Solution:
    def closestPrimes(self, m: int, n: int) -> List[int]:

        is_prime = [True for i in range(n + 1)]
        ans = []
        is_prime[0] = is_prime[1] = False
        i = 2
        
        while i * i <= n:
            if is_prime[i]:
                j = i * i
                while j <= n:
                    is_prime[j] = False
                    j += i
            i += 1
         
           
        arr = []
        for i in range(m, len(is_prime)):
            if is_prime[i]:
                arr.append(i)
                
        if len(arr)<2:
            return [-1,-1]
        
        difference = abs(arr[0]-arr[1])
        ans = [arr[0],arr[1]]
        for i in range(len(arr)-1):
            if  difference > abs(arr[i]-arr[i+1]):
                difference = abs(arr[i]-arr[i+1])
                ans = [arr[i],arr[i+1]]
    
        return ans
 
        