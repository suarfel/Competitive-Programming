class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        elif n%4==0 and n != 0:
            n = n//4
            return self.isPowerOfFour(n) 
        else :
            return False
        