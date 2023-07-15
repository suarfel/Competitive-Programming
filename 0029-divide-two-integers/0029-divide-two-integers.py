class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        val = 0
        if dividend < 0 and divisor > 0:
            val = - (-dividend//divisor)
        if dividend > 0 and divisor < 0:
            val =  - (dividend//-divisor)
        if dividend < 0 and divisor < 0:
            val =  (dividend//divisor)
        if dividend > 0 and divisor > 0:
            val = dividend//divisor
        if val > pow(2,31) -1:
            return pow(2,31) -1
        if val < - pow(2,31):
            return  pow(2,31)
        return val
    