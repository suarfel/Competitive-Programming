class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        arr = []
        n = len(gas)
        for i in range(n):
            arr.append(gas[i] - cost[i])
            
        for i in range(n-2,-1,-1):
            
            arr[i] += arr[i+1]
        
        ans = -1
        max_ = 0
        
        if arr[0] < 0 :
            return -1
        
        for idx,val in enumerate(arr):
            if val >= max_:
                max_ = val
                ans = idx
                
        return ans
            
            
        
        