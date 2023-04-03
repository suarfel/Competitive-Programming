class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        for i in range(n.bit_length()-1):
            if (n & 1<<i) and (n & 1<<i+1) or   (not (n & 1<<i) and not (n & 1<<i+1)):
                return False
        return True