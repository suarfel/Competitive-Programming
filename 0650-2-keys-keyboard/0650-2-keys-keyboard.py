class Solution:
    def minSteps(self, n: int) -> int:
        
        dp_arr = [0]*(n+1)
        dp_arr[1] = 0
        
        def prime_factors(n):
            factors = []
            divisor = 2
            while divisor <= n:
                if n % divisor == 0:
                    factors.append(divisor)
                    n //= divisor
                else:
                    divisor += 1

            return factors
        
        for i in range(2,n+1):
            dp_arr[i] = sum(prime_factors(i))
                        
        return dp_arr[n]
                
