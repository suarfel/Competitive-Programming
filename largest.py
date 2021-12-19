class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        empty_string = []
        largest_number = ""
        sorted_list = []
        if [0]* len(nums) == nums :
            nums = [0]
        for i in range(len(nums)):
            empty_string.append(str(nums[i]))
        for i in range(len(empty_string)-1):
            for j in range(i+1,len(empty_string)):
                if empty_string[i] + empty_string[j]  <  empty_string[j] + empty_string[i]:
                    empty_string[j] ,empty_string[i]= empty_string[i],empty_string[j]
        for i in range(len(empty_string)):
            largest_number = largest_number + empty_string[i]
        return largest_number

 
        