class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        temp_ans = set()
        nums.sort()
        # print(nums)
        i,k = 0,len(nums)-1
        while i < k-1:
            j = i+1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    arr = [nums[i],nums[j],nums[k]]
                    # print(arr)
                    arr.sort()
                    temp_ans.add(tuple(arr))
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
            k = len(nums)-1
        return temp_ans
        
        
    