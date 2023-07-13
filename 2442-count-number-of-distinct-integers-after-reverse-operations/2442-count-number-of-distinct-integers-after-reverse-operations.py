class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            num_set.add(num)
            temp_num = str(num)
            temp_num = temp_num[::-1]
            num_set.add(int(temp_num))
        return len(num_set)
            
            
            
        