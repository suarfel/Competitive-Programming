class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result_list = [-1]*len(nums)
        stack = []
        for i in range(2*len(nums)-1):
            index = i %len(nums)
            print(index)
            while stack and nums[stack[-1]] < nums[index]:
                result_list[stack[-1]] = nums[index]
                stack.pop()
            stack.append(index)
        return result_list
                
        