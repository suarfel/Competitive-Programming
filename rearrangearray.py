class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        li = []
        nums.sort()
        j = len(nums)-1
        for i in range(len(nums)):
            if i <j:
                li.append(nums[i])
                li.append(nums[j])
                j -= 1
            elif i > j:
                return li
            else :
                li.append(nums[i])
                return li
        return li
            
            
                
        