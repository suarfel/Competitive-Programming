class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        counter = 0
        for i in range(len(nums)):
            val = nums[i]
            for j in range(i,len(nums)):
                if nums[j]%k != 0 :
                    break
                val = self.gcd(max(val,nums[j]),min(val,nums[j]))
                if val == k:
                    counter += 1
        return counter
    def gcd(self,large,small):
        if small == 0:
            return large
        return self.gcd(small,large%small)