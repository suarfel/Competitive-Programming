import datetime 
class Solution:
    def closestPrimes(self, m: int, n: int) -> List[int]:
        st1 = datetime.datetime.now()
        is_prime = [True for i in range(n + 1)]
        ans = []
        et1 = datetime.datetime.now()
        print(et1-st1)
        is_prime[0] = is_prime[1] = False
        i = 2
        
        st2 = datetime.datetime.now()
        while i * i <= n:
            if is_prime[i]:
                j = i * i
                while j <= n:
                    is_prime[j] = False
                    j += i
            i += 1
        et2 = datetime.datetime.now()
        print(et2-st2)
       
            
        st3 = datetime.datetime.now()
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
        et3 = datetime.datetime.now()
        print(et3-st3)
                
        return ans
 
        