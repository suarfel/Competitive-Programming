class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = 0
        counter_dict =  {0:1}
        prefix_sum = 0
        for i in nums:
            prefix_sum += i
            if prefix_sum -k in counter_dict:
                counter += counter_dict[prefix_sum -k]
            if prefix_sum in counter_dict:
                counter_dict[prefix_sum] += 1
            else:
                counter_dict[prefix_sum] = 1
        return counter 