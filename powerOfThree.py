class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 0:
            if (n%3==0 and n!=0) or n==1:
                if n==1:
                    return True
                n=n//3
                if n==1:
                    return True
            else:
                return False