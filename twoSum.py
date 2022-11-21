class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set_one = set(nums)
        print(set_one)
        temp  = 0
        for i in range(len(nums)) :
            temp = target - nums[i]
            if temp == target // 2 :
                for x in range(i+1,len(nums)) :
                    if temp + nums[x] == target :
                        return [i,x]
            elif temp in set_one :
                j = nums.index(temp)
                return [i,j]
            else :
                temp = 0