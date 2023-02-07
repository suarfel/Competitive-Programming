class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        prefix_sum = 0
        prefix_dict = {0:-1}
        for i in range(len(nums)):
            if nums[i] == 1:
                prefix_sum += 1
            else:
                prefix_sum -= 1
            if prefix_sum in prefix_dict:
                temp = prefix_dict[prefix_sum]
                tempMax = i - temp
                max_length = max(max_length,tempMax)
            else:
                prefix_dict[prefix_sum] = i
        return max_length
        