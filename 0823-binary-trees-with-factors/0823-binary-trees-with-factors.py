class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        arr.sort()
        counter = defaultdict(int)
        
        for i in range(len(arr)):
            
            ans = 1
            for j in range(len(arr)):
                
                if arr[i] < arr[j]:
                    break
                if arr[i] % arr[j] == 0:
                    ans += counter[arr[j]]*counter[arr[i]//arr[j]]
            counter[arr[i]] = ans
             
        return sum(counter.values())%(pow(10,9) + 7)
                    