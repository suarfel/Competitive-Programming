class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 3:
            return True
        a = 0
        b = int(sqrt(c)) + 1
        while a <= b :
            total = a*a + b*b
            if c ==  total :
                return True
            elif c > total :
                a += 1
            else:
                b -= 1
                
        return False
        