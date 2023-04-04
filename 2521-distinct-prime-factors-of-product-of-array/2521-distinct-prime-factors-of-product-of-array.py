class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        self.factors_set = set()
        d = 2
        n = 1
        for i in nums:
            self.factorization(i)
        return len(self.factors_set)
    def factorization(self,n):
        d = 2
        while d*d <= n:
            while n%d == 0:
                if d not in self.factors_set:
                    self.factors_set.add(d)
                n //= d
            d += 1
        if n > 1:
            self.factors_set.add(n)