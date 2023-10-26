class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:

        nums_set = set(arr)
        arr.sort()
        arr.reverse()
        count_hold = {}
        
        for idx,val in enumerate(arr):
            count_hold[val] = idx 
        
        @lru_cache(None)
        def dp(idx):
            if idx >= len(arr):
                return 0
            ans = 1
            for i in range(idx,len(arr)):
                if arr[idx] % arr[i] == 0 and arr[idx]//arr[i] in nums_set:
                    ans += dp(i)*dp(count_hold[arr[idx]//arr[i]])
            return ans
        
        total = 0
        
        for i in range(len(arr)):
            total += dp(i)
        
        return total % (pow(10,9) + 7)
                    