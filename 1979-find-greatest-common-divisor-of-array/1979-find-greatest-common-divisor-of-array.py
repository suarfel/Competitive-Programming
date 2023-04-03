class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small = min(nums)
        large = max(nums)
        return self.gcd(small,large)
    def gcd(self,large,small):
        if small == 0:
            return large
        return self.gcd(small,large%small)
            
        