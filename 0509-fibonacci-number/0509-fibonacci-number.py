class Solution:
    def fib(self, n: int) -> int:
        
        memo = {}
        
        def fib(n):
            if n == 0 :
                return 0
            elif n == 1 :
                return 1
            if n not in memo:
                memo[n] = fib(n-1) + fib(n-2)
            return memo[n]
        return fib(n)