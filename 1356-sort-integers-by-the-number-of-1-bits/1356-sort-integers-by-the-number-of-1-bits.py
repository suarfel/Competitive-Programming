class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        ans = []
        
        for idx,val in enumerate(arr):
            count = 0
            
            for i in range(14): # Every array element can be at max 10**4
                if 1 << i & val:
                    count += 1
            ans.append((count,val))
        
        ans = sorted(ans)
        
        for idx,ele in enumerate(ans):
            ans[idx] = ele[1]
        
        return ans
        
        
        
                    
            
                
        