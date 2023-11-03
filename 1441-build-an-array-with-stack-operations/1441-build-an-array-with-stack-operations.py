class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
      
        ans = []
        tar_idx = 0
        
        for i in range(1,n+1):
            
            if target[tar_idx] == i :
                ans.append('Push')
                tar_idx += 1
            elif target[tar_idx] > i:
                ans.append('Push')
                ans.append('Pop')
            
            if tar_idx == len(target):
                return ans
            
        return ans
                
        