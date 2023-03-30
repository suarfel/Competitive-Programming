class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        for i in range(64):
            num1 = x & 1 << i
            num2 = y & 1 << i
            if num1 != num2:
                count += 1
        return count
            
        