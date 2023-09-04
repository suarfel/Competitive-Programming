class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        arr = [0]* (len(nums) + 1)
        nums.sort()
        
        for request  in requests:
            arr[request[0]] += 1
            arr[request[1]+1] -= 1
            
        arr.pop()
        
        for i in range(1,len(arr)):
            arr[i] += arr[i-1]
            
        arr.sort()
        
        total = 0
        
        for i in range(len(arr)):
            total += arr[i]*nums[i]
        
        return total % (pow(10,9)+7)
        
        
        