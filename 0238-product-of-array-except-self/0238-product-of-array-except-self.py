class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dic = {}
        product = 1
        ans = []
        for i in range(len(nums)):
            print(i)
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
            if nums[i] == 0:
                continue
            else:
                product *= nums[i]
        print(dic)
        if 0 in dic and dic[0] > 1:
            return [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                temp = [0]* len(nums)
                temp[i] =  product
                return temp
            ans.append(product//nums[i])
        return ans
            

