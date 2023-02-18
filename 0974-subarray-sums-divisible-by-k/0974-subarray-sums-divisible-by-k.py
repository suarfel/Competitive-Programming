class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count_dict = {0:1}
        prefix_sum = 0
        counter = 0
        for i in range(len(nums)):

            prefix_sum += nums[i]
            if prefix_sum%k in count_dict:
                counter += count_dict[prefix_sum%k]
            if prefix_sum%k in count_dict:
                count_dict[prefix_sum%k] += 1
            else :
                count_dict[prefix_sum%k] = 1
        return counter
                
            
        