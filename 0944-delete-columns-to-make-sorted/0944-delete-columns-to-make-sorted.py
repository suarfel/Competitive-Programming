class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        col_len = len(strs[0])
        ans = 0
        for i in range(col_len):
            for j in range(1,len(strs)):
                if strs[j][i] < strs[j-1][i]:
                    ans += 1
                    break
        return ans
                
                
        
    
                
                
        