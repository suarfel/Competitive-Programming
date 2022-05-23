class Solution:
    def myPow(self, x: float, n: int) -> float:
        value = 1
        if n == 0 :
            return 1
        elif n > 0:
            for i in range(n):
                value *= x 
            return value
        else:
            for i in range(abs(n)):
                value *= x
            value = 1/value    
            return value  
        