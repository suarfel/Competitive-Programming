class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum  = 0
        counter = 0
        i = 0
        j = 0
        while i < len(nums):
            # print(sum)
            # print(counter)
            if i == 0 and j == 0:
                sum += nums[i]
                if sum >= target:
                    return 1
                j += 1
            elif sum >= target :
                if counter == 0:
                    counter = j-i 
                elif counter > j - i :
                    counter = j - i 
                    if counter == 1:
                        return 1
                sum -= nums[i]
                i += 1
            else :
                if j == len(nums):
                    return counter
                sum += nums[j]
                j += 1
        return counter
            
                