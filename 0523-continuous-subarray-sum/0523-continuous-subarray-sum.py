class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        counter = {0:-1}
        for i in range(len(nums)):
            prefix += nums[i]
            prefix %= k
            if prefix in counter:
                if i - counter[prefix] > 1:
                    return True
            else :
                counter[prefix] = i
        return False