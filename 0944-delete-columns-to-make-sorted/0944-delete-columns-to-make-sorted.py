class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        col_len = len(strs[0])
        ans = set()
        for i in range(col_len):
            for j in range(1,len(strs)):
                if strs[j][i] < strs[j-1][i]:
                    ans.add(i)
        return len(ans)
                
                
        
    
                
                
        