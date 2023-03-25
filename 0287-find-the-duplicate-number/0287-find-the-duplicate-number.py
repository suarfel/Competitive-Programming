class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                return i
            else:
                dic[i] = 1
    
        # low = 1
        # high = len(nums)-1
        # while low <= high:
        #     mid = low + (high - low)//2
        #     count = 0
        #     for i in nums: 
        #         if low <= i <= high:
        #             if mid >= i:
        #                 count += 1
        #     if count >= (high-low)//2:
        #         low  = mid + 1
        #     else:
        #         high = mid -1
        # return low
    
    
                
            
            
        